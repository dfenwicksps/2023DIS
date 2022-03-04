sentence = "All work and no play makes Jack a dull boy."
list = []
list = sentence.lower().strip('.').split(' ')
for item in list:
    print(item)
