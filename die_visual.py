from die import Die
die = Die()
result_roll = []
for count_num in range(100):
	result_roll.append(die.roll())
print(result_roll)
sum = die.sum_f()
print(sum)
	
