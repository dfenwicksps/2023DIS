# Write a program that calculates the remainder of 10 divided by 3 and prints the result
'''print(10 % 3)  #

if (num1 % num2) == 0:
    # do this, eg add those numbers to a list
else:
    # do that, print or ignore
'''

# Write a program that will print the following multi-line string:
# string1 = "' '' '''"
# ' '' '''
# ' '' '''
'''
for i in range(3):
    print(string1)
print(" ")
for i in range(3):
    print("\' \'\' \'\'\'")
'''
# Evaluate the following numerical expressions in your head, then use print to test the result - note what each OPERATOR
# is used for:

# 5 ** 2

# 9 * 5

# 15 / 12

# 12 / 15

# 15 // 12

# 12 // 15

# 5 % 2

# 9 % 5

# 15 % 12

# 12 % 15

# 6 % 6

# 0 % 7
# Find the prime factors of 1000
# Divide n by 2 1000/2 = 500
# If there is a remainder, stop, and try again with the next largest prime number.
# If there is no remainder, write the denominator/divider down, have n be the product and start again .
# prime factors = 2, 2, 2, 5, 5, 5
# 500/2 = 250/2 = 125/5 = 25/5 = 5
# If the product is a prime, write it down and stop.

# Find the sum of the digits of all numbers from 1 to 100
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 = 66

# Find all prime numbers between 0 and 100


tot = []  # empty list
for i in range(1, 12):  # range of values - could also be replaced with user input
    if i < 10:  # if number is single digit add to 'tot' list
        tot.append(i)
    else:
        num = [int(a) for a in str(i)]  # this line takes the next 3 lines and turns it into one line of code
        # num = []  # create empty list to store multiple digits
        # for a in str(i):
        #    num.append(a)
        for item in num:
            tot.append(item)
print(f"The total is {sum(tot)}")
