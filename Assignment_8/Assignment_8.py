# Read data from input file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Count total lines
print("Total number of lines:", len(lines))

# Write first two lines to a new file
with open("output.txt", "w") as file:
    file.writelines(lines[:2])

print("First two lines are written to output.txt")
