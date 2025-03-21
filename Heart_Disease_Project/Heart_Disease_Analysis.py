import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the heart dataset
df = pd.read_csv('heart.csv')
print(df.head())

# Summary statistics
print(df.describe())

# Set up the visual style for the plots
sns.set(style="whitegrid")

# List of features to visualize
features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

# Set up the plot
plt.figure(figsize=(8, 8))

# Plot histogram for each feature
for i, feature in enumerate(features):
    plt.subplot(5, 3, i+1)
    sns.histplot(df[feature], kde=True, bins=30)
    plt.title(f"Histogram of {feature}")

plt.tight_layout()
plt.show()


# Plot the histogram for the target variable
plt.figure(figsize=(6, 4))
sns.histplot(df['target'], kde=False, bins=2, color='skyblue')

# Add title and labels
plt.title('Histogram of Target (Heart Disease Presence)')
plt.xlabel('Target (0 = No Disease, 1 = Disease)')
plt.ylabel('Count')

plt.show()

# Check for missing values in the 'chol' column
missing_chol = df['chol'].isnull().sum()

print(f"Number of missing values in 'chol' column: {missing_chol}")


# Plot histogram for a Cholisterol feature
plt.figure(figsize=(8, 6))
sns.histplot(df['chol'], bins=20, kde=True, color='skyblue')
plt.title('Histogram of Cholisterol (chol)')
plt.xlabel('Cholestirol')
plt.ylabel('Frequency')
plt.show()



# Plot histogram for a Resting Blood Pressure feature
plt.figure(figsize=(8, 6))
sns.histplot(df['trestbps'], bins=20, kde=True, color='skyblue')
plt.title('Histogram of Resting Blood Pressure (trestbps)')
plt.xlabel('Resting Blood Pressure (mm Hg)')
plt.ylabel('Frequency')
plt.show()

