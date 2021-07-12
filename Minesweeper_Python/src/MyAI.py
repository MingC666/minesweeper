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
		self.uncovered =[]
		self.to_uncovered =[]
		self.move=0
		for i in range(self.row):
				for j in range(self.col):
					self.uncovered.append((i,j))
		self.uncovered.remove((self.x,self.y))
		self.frotier = []
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################


		
	def getAction(self, number: int) -> "Action Object":

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		while(self.move>0):
			temp=self.to_uncovered.pop(0)
			print(temp[0], temp[1])
			self.move-=1
			return Action(AI.Action.UNCOVER, temp[0], temp[1])
		

		# Uncover all if number = 0
		print(self.x, self.y)
		if(0 == number and self.move==0):
			for i in range(self.x-1, self.x+2):
				for j in range(self.y-1, self.y+2):
					# boundary checking
					if(i<0 or i>self.row-1 or j<0 or j>self.col-1):
						continue
					if(i==self.x and j==self.y): #i skip itself
						continue
					self.to_uncovered.append((i,j))
			print(len(self.to_uncovered))
			temp=self.to_uncovered.pop(0)
			self.move=len(self.to_uncovered)
			return Action(AI.Action.UNCOVER, temp[0], temp[1])

		else: #number is 1, then uncover all except its neighboor.
			for i in range(self.row):
				for j in range(self.col):
					#if(i==self.x+1 or i==self.x+1 or)
					if(i-self.x>=-1 and i-self.x<=1  and j-self.y>=-1 and j-self.y<=1):
						continue
					self.to_uncovered.append((i,j))
					self.uncovered.remove((i,j))
					
		while(self.to_uncovered != [] ):
			temp = self.uncovered.pop(0)
			return Action(AI.Action.UNCOVER, temp[0], temp[1])
		
		#return Action(AI.Action.LEAVE)
		
		


		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
