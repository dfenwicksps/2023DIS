# Get a number
n = int(input("Enter a number: "))
print(type(n))
# Create a list to store prime numbers
primes = []
quotient = []
# Divide n by 2
# num = int(n/2)
# print(type(num))
# If there is a remainder, stop, and try again with the next largest prime number.
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
while n != 1:
    for prime in prime_numbers:
        # if n % prime == 0:
        n = n / prime
        primes.append(prime)
        quotient.append(n)

# If there is no remainder, write the denominator/divider down, have n be the product and start again
# primes.append(num)
# If the product is a prime, write it down and stop.
print(primes)
print(quotient)
