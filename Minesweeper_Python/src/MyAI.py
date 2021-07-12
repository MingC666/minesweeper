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
		self.x = startX 
		self.y = startY
		self.lastx = startX
		self.lasty = startY
		self.beginPoint = (startX, startY)
		

		self.covered = []
		self.to_uncovered = []
		self.safelist = []
		#initial covered list
		#for i in range(self.row-1):
			#for j in range(self.col-1):
					#self.covered.append((i,j))
			
		#initial map list
		rows, cols = (self.row, self.col)
		self.map = [[-1 for i in range(cols)] for j in range(rows)]

		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################


		
	def getAction(self, number: int) -> "Action Object":

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		

		# Uncover all if number = 0
		if(0 == number):
			self.safelist.append((self.lastx, self.lasty))
			for i in range(max(self.lastx-1,0),min(self.col,self.lastx+2)):
				for j in range(max(self.lasty-1,0),min(self.row,self.lasty+2)):
					self.map[i][j] = 0
					if((i,j)!=self.beginPoint and ((i,j) not in self.safelist) and ((i,j) not in self.to_uncovered)):
						self.to_uncovered.append((i,j))
			

		else: #number is 1
			self.map[self.lastx][self.lasty] = number


		if(self.to_uncovered != []):
			temp = self.to_uncovered.pop(0)
			self.lastx=temp[0]
			self.lasty=temp[1]
			return Action(AI.Action.UNCOVER, temp[0], temp[1])


	
		#if(self.to_uncovered != []):
			#temp = self.to_uncovered.pop(0)
			#return Action(AI.Action.UNCOVER, temp[0], temp[1])
		for i in range(self.row):
			for j in range(self.col):
				if self.map[i][j] == -1:
					self.covered.append((i,j))


		count = 0
		minelist = []
		for i in range(1, self.row-1):
			for j in range(1, self.row-1):
				if (self.map[i][j]) == -1:
					minelist.append((i,j))
					count += 1
		
		if(count == 1):
			self.covered.remove(minelist[0])

		for tile in self.covered:
			return Action(AI.Action.UNCOVER, tile[0], tile[1])

			# check if the map temparr  are all 0, if yes, (j,k) are mine, uncovered all self.covered except (j,k)


				

   					 
							
							 
	
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
