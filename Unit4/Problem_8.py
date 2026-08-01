import numpy as np
import pandas as pd

items = ["Rice", "Sugar", "Oil", "Soap", "Milk"]
price = np.array([60, 45, 180, 35, 55])
quantity = [15, 8, 12, 5, 20]

print("Mean =", np.mean(price))
print("Median =", np.median(price))
print("Maximum =", np.max(price))
print("Minimum =", np.min(price))

df = pd.DataFrame({
    "Item": items,
    "Price": price,
    "Quantity": quantity
})

print("\nDataFrame")
print(df)

print("\nItems having quantity less than 10")
print(df[df["Quantity"] < 10])