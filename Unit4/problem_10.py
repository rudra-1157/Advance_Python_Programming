import numpy as np
import pandas as pd

rooms = ["A101", "A102", "A103", "A104", "A105"]
rent = np.array([2500, 4500, 3500, 6000, 5000])

print("Mean =", np.mean(rent))
print("Median =", np.median(rent))
print("Maximum =", np.max(rent))
print("Minimum =", np.min(rent))

df = pd.DataFrame({
    "Room": rooms,
    "Rent": rent
})

print("\nDataFrame")
print(df)

print("\nRooms having rent greater than 4000")
print(df[df["Rent"] > 4000])