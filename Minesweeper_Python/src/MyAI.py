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
		self.covered = []
		#initial covered list
		for i in range(self.row-1):
				for j in range(self.col-1):
					self.covered.append((i,j))
			
		#initial map list
		rows, cols = (self.row, self.col)
		self.map = [[-1 for i in range(cols)] for j in range(rows)]

		self.to_uncovered = []
		self.covered = []
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################


		
	def getAction(self, number: int) -> "Action Object":

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		

		# Uncover all if number = 0
		if(0 == number):
			self.map[self.x][self.y] = 0
			self.covered.remove((self.x,self.y))
			for i in range(self.x-1, self.x+2):
				for j in range(self.y-1, self.y+2):
					# boundary checking
					if(i<0 or i>self.row-1 or j<0 or j>self.col-1):
						continue
					if(i==self.x and j==self.y): #i skip itself
						continue
					self.to_uncovered.append((i,j))
			

		else: #number is 1
			self.map[self.x][self.y] = 1
			self.covered.remove((self,x,self,y))


		if(self.to_uncovered != []):
			temp = self.to_uncovered.pop(0)
			return Action(AI.Action.UNCOVER, temp[0], temp[1])


	
		if(self.to_uncovered != []):
			temp = self.to_uncovered.pop(0)
			return Action(AI.Action.UNCOVER, temp[0], temp[1])


		if(len(self.dangerous)==1):
			t=self.dangerous.pop(0)
			return Action(AI.Action.FLAG, t[0], t[1])

		else:
			#Testing mine, for that dangerous tile, if all its neighbor -1 and there are not more 1, then it is mine	
			temparr = list(map(list, self.map))
			# for each dangerous
			for (j,k) in self.dangerous:
				#all its surrounding -1
				for j in range(self.x-1, self.x+2):
					for k in range(self.y-1, self.y+2):
						if(j<0 or j>self.row-1 or k<0 or k>self.col-1):
							continue
						temparr[j][k] -= 1
				# check the map if there are all 0
				for i in range(len(temparr)):
   					 for j in range(len(temparr[i])):
						if(temparr[i][j]==1):
							fla=False
							
							 
				
		# uncovered all reset tile
		#return Action(AI.Action.LEAVE)
		
		


		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
