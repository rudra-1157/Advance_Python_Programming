import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

brand = input("Enter Brand Name: ")

with open(args.filename, "r") as file:
    reader = csv.DictReader(file)

    print("\nAll Mobile Records")
    for row in reader:
        print(row)

file = open(args.filename, "r")
reader = csv.DictReader(file)

print("\nMatching Records")
for row in reader:
    if row["Brand"].lower() == brand.lower():
        print(row)

file.close()