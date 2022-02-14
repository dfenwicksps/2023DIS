# Checks for a number in a range
# num = int(input("Enter a number: "))
def rangecheck(num):  # this is called a function declaration
    min = 0
    max = 100
    for i in range(min, max):  # loop that continues for a known number of iterations
        # print(i)
        # if num in range(0, 100):
        if num > min and num < max:  # conditional statement
            print(num)
            # exit()  # will exit the current program
            break  # break will exit the current loop
        else:
            print(f"Number {num} not in range {min} to {max}.")
            # exit()
            break


# Once I have declared/created a function, I need to make a FUNCTION CALL
rangecheck(140)
rangecheck(20)
for i in range(1, 51):
    a = i
    b = i * 10
    rangecheck(a)
    rangecheck(b)
    a += i
    b -= i
