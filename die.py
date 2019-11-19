from random import randint
"""表示一个骰子类"""
class Die():
	def __init__(self,num_side=6):
		self.num_side = num_side
		self.sum = 0
	def roll(self):
		return  randint(1,self.num_side)
	def sum_f(self):
		i = 0
		while i < self.num_side:
			self.sum += i
			i = i +1
		return self.sum
	
