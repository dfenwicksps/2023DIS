# Euclids algorithm
# Take 2 numbers
# Divide second into first
# Take remainder and divide into previous divisor
# eg 60 and 8
# 60 / 8 = 7 r 4; 8 / 4 = 2
# so GCD of 60 and 8 is 4


def gcd(a, b):
    while (b != 0):
        t = a  # set a as a temp variable t
        a = b  # put b into a
        b = t % b  # divide b into a, continue until zero
    return a


print(gcd(60, 8))
print(a)
print(gcd(20, 8))
print(a)
print(gcd(60, 96))
print(a)
