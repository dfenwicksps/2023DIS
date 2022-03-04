# To find the prime factors of 1000 using the division method,
#  Start dividing 1000 from the smallest prime number i.e., 2, 3, 5, and so on, and find the smallest prime factor of the number.
#  After finding the smallest prime factor of the number 1000, which is 2, divide 1000 by 2 to obtain the quotient 500.
#  Hence 500 and 2 are the factors of 1000.
# Repeat step 1 with the obtained quotient (500) and continue until you reach quotient as 1.
# So, the Prime factorization of 1000 is 2 × 2 × 2 × 5 × 5 × 5.
n = 1000
# prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
factors = []
while n != 1:  # initially this was n > 0 but found I was left with 1 at end which I would have known if I'd read the algorithm more carefully
    if n % 2 == 0:
        n = n / 2
        factors.append(2)
        print("1")  # use print statements to help desk-check/error check
        print(factors)
        print(n)
    elif n % 3 == 0:
        n = n / 3
        factors.append(3)
        print("2")
        print(factors)
        print(n)
    elif n % 5 == 0:
        n = n / 5
        factors.append(5)
        print("3")
        print(factors)
        print(n)
print(factors)
