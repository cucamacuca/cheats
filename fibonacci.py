#fibonacci

def fibonacci(value):
    if (value <= 1):
        return value
    return fibonacci(value - 1) + fibonacci(value - 2)

def fibonacci_iterative(value):
	ant_sum = 0
	last_sum = 1

	if (value <= 1):
		return value

	for k in range(1, value):
		tmp = last_sum
		last_sum = ant_sum + last_sum
		ant_sum = tmp

	return last_sum


print fibonacci(0) #0
print fibonacci(1) #1
print fibonacci(2) #1
print fibonacci(3) #2
print fibonacci(4) #3
print fibonacci(5) #5

print fibonacci_iterative(0) #0
print fibonacci_iterative(1) #1
print fibonacci_iterative(2) #1
print fibonacci_iterative(3) #2
print fibonacci_iterative(4) #3
print fibonacci_iterative(5) #5