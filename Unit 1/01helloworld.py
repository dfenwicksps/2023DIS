'''import this  # the zen of Python!

print("Hello, World!")
name = "David"
print("My name is", name + ".")  # using variables in a string
teacher = "Mr Fenwick"
print(f"Your teacher is {teacher}.")  # using an f-string with variables <- preferred choice
'''
print("# Squares List - multi line version")
squares = []  # create an empty list
for i in range(10):  # running a loop 10 times, beginning with 0
    squares.append(i ** 2)
print(squares)

print("# Squares - One line version")
print([i ** 2 for i in range(10)])
