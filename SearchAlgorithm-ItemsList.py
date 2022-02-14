# Input - numbers in a list
# Output - highest number

# Read list of numbers
numbers = [4, 3, 315, 8, 65, 119, 205, 20, 5]
largest = 0
for num in numbers:  # For each number
    if num > largest:  # If larger than Largest
        largest = num  # Add to Largest
print(largest)  # Print Largest
