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
		self.to_covered = []
		self.dangerous = []
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################


		
	def getAction(self, number: int) -> "Action Object":

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		

		# Uncover all if number = 0
		if(0 == number):
			for i in range(self.x-1, self.x+2):
				for j in range(self.y-1, self.y+2):
					# boundary checking
					if(i<0 or i>self.row-1 or j<0 or j>self.col-1):
						continue
					if(i==self.x and j==self.y): #i skip itself
						continue
					if((i,j) in self.dangerous):  #if '0' 's neigher is dangerous, then remove it from dangerous
						self.dangerous.clear((i,j))
					self.covered.append((i,j))
					self.to_covered.append((i,j))

		else: #number is 1, all its uncovered neighboor are dangerous
			for i in range(self.x-1, self.x+2):
				for j in range(self.y-1, self.y+2):
					# boundary checking
					if(i<0 or i>self.row-1 or j<0 or j>self.col-1):
						continue
					if(i==self.x and j==self.y): #i skip itself
						continue
					self.dangerous.append((i,j))
		
		if(self.to_covered!=[]):
			temp = self.to_uncovered.pop(0)
			return Action(AI.Action.UNCOVER, temp[0], temp[1])
					
		# uncovered all reset tile
		#return Action(AI.Action.LEAVE)
		
		


		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
