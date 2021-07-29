# ==============================CS-199==================================
# FILE:			MyAI.py
#
# AUTHOR: 		Justin Chung
#
# DESCRIPTION:	This file contains the MyAI class. You will implement your
#				agent in this file. You will write the 'getAction' function,
#				the constructor, and any additional helper functions.
#
# NOTES: 		- MyAI inherits from the abstract AI class in AI.py.
#
#				- DO NOT MAKE CHANGES TO THIS FILE.
# ==============================CS-199==================================

import random
from AI import AI
from Action import Action


class MyAI( AI ):

	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		self.row = rowDimension
		self.col =  colDimension
		self.totalMines = totalMines
		if(startX>self.row-1):
			temp=startX
			startX = startY
			startY = temp
		self.x = startX
		self.y = startY
		

		self.covered = []
		self.to_uncovered = []
		self.minelist = []
		self.checkedlist = []
		self.frontier_cover = []
		self.frontier_uncover = []

		self.changedlist = []				#store position where the effective number changed caused by mine

		# initial the simulating board
		self.map = [[-1 for i in range(self.col)] for j in range(self.row)]	# the map track all affective number in the board, # -1:covered; 10:mine

		#initial covered list
		for i in range(self.row):
			for j in range(self.col):
					if(i==self.x and j==self.y):
						continue
					self.covered.append((i,j))
		#remove initial tile from covered list			
		#self.covered.remove((self.x,self.y))

		# add fisrt checked point
		self.checkedlist.append((self.x, self.y))
		# add first frontie_uncovered & frontie_covered
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################




	def getAction(self, number: int) -> "Action Object":
		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		"""print("Now, ", (self.x,self.y), "=", number, "Before change the map[][]:")
		for i in self.map:
			print(i)"""
		
		#########################################################
		#################### update the number in the board #####
		#
		# updating the number to simulating self.map
		if(self.map[self.x][self.y]==-1 and number!=-1):
			self.map[self.x][self.y] = number
			
		
		
		
		#########################################################
		#################### Checking the returning NUMBER (newest uncovered tile) 
		#
		#####*****number=-1, it's a MINE******####
		# if MINE is found, the surrounding uncovered effective number need -1, updating them in the self.map[][]
		if(-1==number):
			"""print("the MINE is in ", (self.x, self.y),"before change map:")
			for i in self.map:
				print(i)"""
			self.itsMine(self.x, self.y)

		# number = 0; uncovered all surrounding covered tiles
		if(0 == number): 
			for i in range(self.x-1, self.x+2):
				for j in range(self.y-1, self.y+2):
					# boundary checking
					if(i<0 or i>self.row-1 or j<0 or j>self.col-1):
						continue
					if((i,j) not in self.checkedlist):
						#print("I am in 000 area!! ", (self.x,self.y), "will add to_uncovered", (i,j) )
						self.checkedlist.append((i,j))		# mark that the tile is checked
						self.to_uncovered.append((i,j))


		# if number>0, and there are mines around, change the NUMBER in simulating board by -#MINE
		if(number>0 and self.mineNum(self.x,self.y)>0):
			#print("uncovered a tile with mine around")
			self.map[self.x][self.y] -= self.mineNum(self.x,self.y)
			
		"""print("After change the map[][], it looks like:")
		for i in self.map:
			print(i)"""

		#########################################################
		#################### if no more tile adding, start uncovereed tiles 
		#
		# 							
		if(self.to_uncovered != []):
			#print(len(self.checkedlist))
			#print("remove", (self.x,self.y), "fromg to_uncovered")
			temp = self.to_uncovered.pop(0)
			self.x = temp[0]
			self.y = temp[1]
			self.covered.remove((self.x, self.y))
			#print(len(self.covered), " tiles are covered")
			#print("it going to uncovered ", (self.x, self.y) )
			if(self.row != self.col):
				return Action(AI.Action.UNCOVER, self.y, self.x)
			else:
				return Action(AI.Action.UNCOVER, self.x, self.y)

		if(self.minelist != []):
			temp = self.minelist.pop(0)
			self.x = temp[0]
			self.y = temp[1]
			self.covered.remove((self.x, self.y))
			self.totalMines -= 1
			#print(len(self.covered), " tiles are covered")
			if(self.row != self.col):
				return Action(AI.Action.FLAG, self.y, self.x)
			else:
				return Action(AI.Action.FLAG, self.x, self.y)
		#########################################################
		#################### Frontier list updating #############
		#
		#print(len(self.covered))
		if(len(self.covered)==0):
			return Action(AI.Action.LEAVE)
		self.frontier_cover = []
		self.frontier_uncover = []
		# getting frontier_uncovered from checked list, if the tile has covered tiles surrounded
		for (i,j) in self.checkedlist:
			if(self.coveredNum(i,j) > 0 and (i,j) not in self.frontier_uncover):
				self.frontier_uncover.append((i,j))
		for (i,j) in self.covered:
			if(self.uncoveredNum(i,j)>0):
				self.frontier_cover.append((i,j))
		#print("front_uncovered are ", self.frontier_uncover)
		#print("front_covered are ", self.frontier_cover)

		#########################################################
		#################### Frontier list checking #############
		#
		# if frontier_uncovered effecitve number=0, uncovered all surrounding
		for (i,j) in self.frontier_uncover:
			# uncovered those surrounding by NUMBER=0
			if(0==self.map[i][j] and self.coveredNum(i,j)>0):
				for r in range(i-1, i+2):
					for c in range(j-1, j+2):
						# boundary checking
						if(r<0 or r>self.row-1 or c<0 or c>self.col-1):
							continue
						if((r,c) not in self.checkedlist):
							print("find a 0 in frontier ", (i,j),", and adding", (r,c), "for uncovered")
							self.checkedlist.append((r,c))		# mark that the tile is checked
							self.to_uncovered.append((r,c))
							
							

			# if frontier_uncovered effecitve number=#covered, they are MINEs
			if(self.coveredNum(i,j)==self.map[i][j]):							
				# finde that mine
				#print("now in frontier ",(i,j), " fingding a MINE")
				for n in range(i-1, i+2):
					for m in range(j-1, j+2): 
						# boundary checking
						if(n<0 or n>self.row-1 or m<0 or m>self.col-1):
							continue 
						if(self.map[n][m]==-1 and (n,m) not in self.minelist):
							"""if(n==0 and m==5):
								print("lllllllllllllllist")
								for i in self.map:
									print(i)
							print("found a mine in ", (n,m))"""
							#print("found a mine in frontier_uncovered", (n,m))
							self.checkedlist.append((n,m))
							self.minelist.append((n,m))


		if(self.to_uncovered != []):		
			#print(len(self.checkedlist))
			temp = self.to_uncovered.pop(0)
			self.x = temp[0]
			self.y = temp[1]
			self.covered.remove((self.x, self.y))
			if(self.row != self.col):
				return Action(AI.Action.UNCOVER, self.y, self.x)
			else:
				return Action(AI.Action.UNCOVER, self.x, self.y)

		if(self.minelist != []):
			temp = self.minelist.pop(0)
			self.x = temp[0]
			self.y = temp[1]
			self.covered.remove((self.x, self.y))
			self.totalMines -= 1
			if(self.row != self.col):
				return Action(AI.Action.FLAG, self.y, self.x)
			else:
				return Action(AI.Action.FLAG, self.x, self.y)

		################################################################################
		################# IF THERE ARE NOT HINT FROM UNCOVERED TILE TO GET NEXT UNCOVERED TILE
		################################################################################
		if(len(self.covered)>0):
			#print("Not more tile can be uncovered by hint, active method 1&2")
			############# METHOD 1 ##################################
			"""temp = self.covered.pop(random.randrange(len(self.covered)))
			self.x = temp[0]
			self.y = temp[1]
			self.covered.remove((self.x, self.y))
			return Action(AI.Action.UNCOVER, temp[0], temp[1])"""

			
			############# METHOD 2 ##################################
			# uncovered 4 corner of the board
			if(self.map[0][0]==-1):
				self.covered.remove((0,0))
				self.checkedlist.append((0,0))
				self.x=0
				self.y=0
				return Action(AI.Action.UNCOVER, 0, 0)
			elif(self.map[0][self.col-1]==-1):
				self.covered.remove((0,self.col-1))
				self.checkedlist.append((0,self.col-1))
				self.x=0
				self.y=self.col-1
				return Action(AI.Action.UNCOVER, 0, self.col-1)
			elif(self.map[self.row-1][0]==-1):
				self.covered.remove((self.row-1,0))
				self.checkedlist.append((self.row-1,0))
				self.x=self.row-1
				self.y=0
				return Action(AI.Action.UNCOVER, self.row-1, 0)
			elif(self.map[self.row-1][self.col-1]==-1):
				self.covered.remove((self.row-1,self.col-1))
				self.checkedlist.append((self.row-1,self.col-1))
				self.x=self.row-1
				self.y=self.col-1
				return Action(AI.Action.UNCOVER, self.row-1, self.col-1)
			else:		# all cornor are uncovered, using method 1
				#print("active random AI")
				temp = self.covered.pop(random.randrange(len(self.covered)))
				self.x = temp[0]
				self.y = temp[1]
				#print("ther random is ", (self.x, self.y))
				self.checkedlist.append((self.x, self.y))
			if(self.row != self.col):
				return Action(AI.Action.UNCOVER, self.y, self.x)
			else:
				return Action(AI.Action.UNCOVER, self.x, self.y)



		return Action(AI.Action.LEAVE)	
							 


	#####################################
	########### HELP FUNCTION ###########
	#####################################

	##############################
	# return the number of covered tiles around the tile(x,y)
	def coveredNum(self, x, y):
		num=0
		for i in range(x-1, x+2):
			for j in range(y-1, y+2): 
				# boundary checking
				if(i<0 or i>self.row-1 or j<0 or j>self.col-1):
					continue 
				if(self.map[i][j] == -1):
					num+=1
		return num

	##############################
	# return the number of uncovered tiles around the tile(x,y)
	def uncoveredNum(self, x, y):
		num=0
		for i in range(x-1, x+2):
			for j in range(y-1, y+2): 
				# boundary checking
				if((i,j) in self.checkedlist):
					num+=1
		return num

	##############################
	# return the number of mine that surrounding by (x,y)
	def mineNum(self, x, y):
		# check surrounding
		num=0
		for i in range(x-1, x+2):
			for j in range(y-1, y+2): 
				# boundary checking
				if(i<0 or i>self.row-1 or j<0 or j>self.col-1):
					continue 
				if(self.map[i][j] == 10):
					num+=1
		return num

	##############################	
	# checking the current posistion is frontier or not
	def frontierCheck(self, x, y):
		numb = 0
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):  
				# boundary checking
				if(i<0 or i>self.row-1 or j<0 or j>self.col-1):
					continue 
				if(self.map[i][j] == -1):
					self.frontier_cover.append((i,j))
					numb =+ 1

		if(numb>0 and (x,y) not in self.frontier_uncover):
					self.frontier_uncover.append((x,y))


	##############################
	# updating the simulating board, if it is a mine, all surrounding uncovered tile number -1
	def itsMine(self, x, y):
		self.map[x][y] = 10
		for i in range(x-1, x+2):
			for j in range(y-1, y+2): 
				# boundary checking
				if(i<0 or i>self.row-1 or j<0 or j>self.col-1):
					continue 

				if(i==x and j==y): # mine position, skip
					continue

				if((self.map[i][j]!=-1) and self.map[i][j]!=10 ): # for all uncovered tile, effective number -1
					#print("mine is ", (x,y), " changing the position ", (i,j))
					#self.changedlist.append((i,j))
					self.map[i][j] -= 1
		#print("these posisitions' effective number has changed")
		#print(self.checkedlist)
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
