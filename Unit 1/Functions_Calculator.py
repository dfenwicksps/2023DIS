# create a function that takes 2 numbers and MULTIPLIES them, returning the result
def multiply(num1, num2):
    return print(num1 * num2)


# create a function that takes 2 numbers and DIVIDES he second from the first, returning the result
def divide(num1, num2):
    return int(num1 / num2)


# create a function that takes 2 numbers and ADDS them, returning the result
def add(num1, num2):
    result = num1 + num2
    print(result)


# create a function that takes 2 numbers and MINUSES the second from the first, returning the result
def minus(num1, num2):
    result = num1 - num2
    return result


# FUNCTION CALLS
multiply(20, 5)
print(divide(1000, 10))
add(65, 35)
# print(result)  # result is unknown - because we are trying to access it outside of the function
print(minus(147, 47))  # here result is returned in the function and printed to screen

# each of the above functions should print 100 as an INTEGER
20, 5
1000, 10
65, 35
147, 47
# Extension:
# How can you make your calculator more useable??
# How can you make the output more informative??
