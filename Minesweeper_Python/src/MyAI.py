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
		self.frotier = []
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################


		
	def getAction(self, number: int) -> "Action Object":

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		
		# Uncover all if number = 0
		if(0 == number):
			for i in range(self.x-1, self.x+1):
				for j in range(self.h-1, self.j+1):
					# boundary checking
					if(i<0 or i>self.row or j<0 or j>self.col):
						continue
					Action(AI.Action.UNCOVER, i, j)
					self.frotier.append((i,j))

		else: #number is 1, then uncover all except its neighboor.
			for i in range(self.row):
				for j in range(self.col):
					#if(i==self.x+1 or i==self.x+1 or)
					if(i-self.x>=-1 and i-self.x<=1  and j-self.y>=-1 and j-self.y<=1):
						continue
					Action(AI.Action.UNCOVER, i, j)
					
					self.frotier.append((i,j))

		
		#return Action(AI.Action.LEAVE)
		
		


		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################

