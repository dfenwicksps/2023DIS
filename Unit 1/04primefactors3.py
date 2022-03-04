# To find the prime factors of 1000 using the division method,
#  Start dividing 1000 from the smallest prime number i.e., 2, 3, 5, and so on, and find the smallest prime factor of the number.
#  After finding the smallest prime factor of the number 1000, which is 2, divide 1000 by 2 to obtain the quotient 500.
#  Hence 500 and 2 are the factors of 1000.
# Repeat step 1 with the obtained quotient (500) and continue until you reach quotient as 1.
# So, the Prime factorization of 1000 is 2 × 2 × 2 × 5 × 5 × 5.
run = "y"
while run == "y":
    n = int(input("Enter a number: "))
    orig = n
    pn = [2, 3, 5, 7, 11, 13, 17, 19]
    i = 0
    factors = []
    while n != 1:  # initially this was n > 0 but found I was left with 1 at end
        if n % pn[i] == 0:
            n = n / pn[i]
            factors.append(pn[i])
            # print(factors)
            # print(n)
        else:
            i = i + 1
    print(f"The prime factors of {orig} are: {', '.join(str(elem) for elem in factors)}")
    run = input("Would you like to run again? (y/n) ").lower()
print("Thanks for using my program.")
