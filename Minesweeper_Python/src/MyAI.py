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
		self.to_uncovered = []
		self.checkedlist = []

		# add fisrt checked point
		self.checkedlist.append((self.x, self.y))
		
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################


	def getAction(self, number: int) -> "Action Object":

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		
		# Uncover all surrounding that not uncovered yet, if number = 0

		if(0 == number and len(self.checkedlist)<self.row*self.col-self.totalMines):  # number of unchecked < total tile - #mine
				# i=2, j=0
				# rang(1,4)
			for i in range(self.x-1, self.x+2):
				for j in range(self.y-1, self.y+2):
					# boundary checking
					if(i<0 or i>self.row-1 or j<0 or j>self.col-1):
						continue
					if((i,j) not in self.checkedlist):
						#print("I am in 000 area!! ", (self.x,self.y), "will uncovered", (i,j) )
						self.checkedlist.append((i,j))
						self.to_uncovered.append((i,j))
		
		
		# checking if unmber is not 0
		if(number!=0 and len(self.checkedlist)<self.row*self.col-self.totalMines):  # number of unchecked < total tile - #mine
			for i in range(self.row):
				for j in range(self.col):
					if( (i>self.x-1 and i<self.x+2) or (j>self.y-1 and j<self.y+2) ):
						continue
					if( (i,j) not in self.checkedlist or (i,j) in self.covered):
						#print("I am in MINE area!! ", (self.x,self.y), "will uncovered", (i,j) )
						self.checkedlist.append((i,j))
						self.to_uncovered.append((i,j))

		if(self.to_uncovered != []):
			#print(len(self.checkedlist))
			temp = self.to_uncovered.pop(0)
			self.x = temp[0]
			self.y = temp[1]
			return Action(AI.Action.UNCOVER, temp[0], temp[1])


		return Action(AI.Action.LEAVE)	
							 
	
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
