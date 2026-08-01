import csv
import re

# Display all books
with open("books.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Book Records")
    for row in reader:
        print(row)

# Search books
keyword = input("\nEnter title keyword: ")

with open("books.csv", "r") as file:
    reader = csv.DictReader(file)

    print("\nMatching Books")
    for row in reader:
        if re.match(keyword, row["Title"], re.IGNORECASE):
            print(row)