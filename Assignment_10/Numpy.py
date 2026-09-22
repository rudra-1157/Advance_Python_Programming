import numpy as np

# Create a one-dimensional array containing values from 1 to 10.
numbers = np.arange(1, 11)
print("Original array:", numbers)

# Slicing operations.
print("First five elements:", numbers[:5])
print("Elements from index 3 to 7:", numbers[3:8])
print("Every alternate element:", numbers[::2])

# Statistical measures.
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

# Broadcasting: add 10 to every array element.
modified_numbers = numbers + 10
print("After broadcasting (+10):", modified_numbers)
