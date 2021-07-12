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
		self.to_uncovered = []
		self.covered = []
		self.danger = []
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
		

		# Uncover all if number = 0
		if(0 == number):
			for i in range(self.x-1, self.x+2):
				for j in range(self.y-1, self.y+2):
					# boundary checking
					if(i<0 or i>self.row-1 or j<0 or j>self.col-1):
						continue
					if(i==self.x and j==self.y): #i skip itself
						continue
					self.to_uncovered.append((i,j))
					self.uncovered.append((i,j))

		elif(1==number and self.totalMines!=0): #number is 1, find the one that only have 1 covered, which is mine--- only for 5*5
			count = 0
			for i in range(self.x-1, self.x+2):
				for j in range(self.y-1, self.y+2):
					if((i,j) not in self.uncovered):
						tx=i
						ty=j
						count+=1
			if(count ==1 ):  #find mine is found
				# add all tile to_uncovered
				self.totalMines-=1
				for j in range(self.row-1):
					for k in range(self.col-1):
						if(i,j) not in self.covered:
							self.uncovered.append((j,k))
							self.to_uncovered.append((j,k))

		while(self.to_uncovered != []):
			temp = self.to_uncovered.pop(0)
			return Action(AI.Action.UNCOVER, temp[0], temp[1])
					
		# uncovered all reset tile
		#return Action(AI.Action.LEAVE)
		
		


		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
