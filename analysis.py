import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    "Name": ["Sanjay", "Rahul", "Anita", "Kiran", "Meena"],
    "Hours_Studied": [2, 4, 3, 5, 1],
    "Marks": [55, 75, 65, 90, 50]
}

df = pd.DataFrame(data)

# Basic Analysis
print("\n=== DATA ===")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Max Marks:", df["Marks"].max())
print("Min Marks:", df["Marks"].min())

# Visualization
plt.scatter(df["Hours_Studied"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()

