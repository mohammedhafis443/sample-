import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 78, 92, 60, 74],
    'Science': [88, 74, 95, 58, 80],
    'English': [90, 82, 85, 65, 78]
}

df = pd.DataFrame(data)


df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

print("Student Marks Data:\n", df)
print("\nClass Average per Subject:\n", df[['Math', 'Science', 'English']].mean())

# -----------------------------
# Step 3: Plotting
# -----------------------------

# 1. Bar chart - Total marks per student
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Total'], color='skyblue', edgecolor='black')
plt.title('Total Marks per Student')
plt.xlabel('Student')
plt.ylabel('Total Marks')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 2. Line chart - Subject-wise marks
plt.figure(figsize=(8, 5))
for subject in ['Math', 'Science', 'English']:
    plt.plot(df['Name'], df[subject], marker='o', label=subject)
plt.title('Subject-wise Marks')
plt.xlabel('Student')
plt.ylabel('Marks')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 3. Box plot - Distribution of marks per subject
plt.figure(figsize=(8, 5))
df[['Math', 'Science', 'English']].plot(kind='box')
plt.title('Marks Distribution per Subject')
plt.ylabel('Marks')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

data = {
    'Temperature': [28, 30, 32, 31, 29, 27, 33],
    'Humidity': [70, 65, 60, 62, 68, 75, 55],
    'Rainfall': [5, 0, 0, 2, 10, 15, 0]  # in mm
}

df = pd.DataFrame(data)

# Scatter plot: Temp vs Humidity, color by Rainfall
plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    df['Temperature'],
    df['Humidity'],
    c=df['Rainfall'],
    cmap='Blues',
    s=100,
    edgecolors='black'
)

plt.colorbar(scatter, label='Rainfall (mm)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.title('Temperature vs Humidity (Colored by Rainfall)')
plt.grid(True)
plt.show()

