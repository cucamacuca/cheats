import math

#combination without repetition
def combination(total, number):
	return math.factorial(total) / (math.factorial(number) * math.factorial(total - number))

#combination with repetition
def combination_rep(total, number):
	return math.factorial(total + number - 1) / (math.factorial(number) * math.factorial(total - 1))

#A Permutation is an ordered Combination. 
#Permutation without repetition
def permutation(total, number):
	return math.factorial(total) / (math.factorial(total - number))

#Permutation with repetition
def permutation_rep(total, number):
	return int(math.pow(total, number))

print combination(4,2) #6
print combination(16,3) #560
print combination(1,1) #1

print combination_rep(5,3) #35

print permutation(16,3) #3360
print permutation(10,2) #90
print permutation_rep(2,3) #8
print permutation_rep(10,3) #1000
print permutation_rep(10,4) #10000