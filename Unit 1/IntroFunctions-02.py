# explain try/except
# show basic functions
# num = int(input("Enter a number: "))
def rangecheck(num):
    # min/max
    for i in range(0, 100):
        # print(i)
        # if i in range(0, 100):
        if i > 0 and i < 100:
            if num == i:
                print("Num is ", i)
                # exit()
            else:
                continue
        else:
            print("Sorry your number isn't in this range.")


rangecheck(155)
