import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer  # Importing SimpleImputer

# Load your dataset (assuming it's in CSV format)
df = pd.read_csv('heart.csv')

# Show the first few rows of the data
print(df.head())

# Check basic info about the dataset (null values, datatypes)
print(df.info())

# Check descriptive statistics
print(df.describe())

# List of features to visualize
features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

# Set up the plot
plt.figure(figsize=(12, 12))

# Plot histogram for each feature
for i, feature in enumerate(features):
    plt.subplot(5, 3, i+1)
    sns.histplot(df[feature], kde=True, bins=30)
    plt.title(f"Histogram of {feature}")

plt.tight_layout()
plt.show()

# Convert 'cp' (chest pain type) to numerical values
cp_map = {0: 'typical angina', 1: 'atypical angina', 2: 'non-anginal pain', 3: 'asymptomatic'}
df['cp'] = df['cp'].map({val: idx for idx, val in enumerate(cp_map)})

# Convert 'restecg' (resting electrocardiographic results) to numerical values
restecg_map = {0: 'normal', 1: 'having ST-T wave abnormality', 2: 'showing probable left ventricular hypertrophy'}
df['restecg'] = df['restecg'].map({val: idx for idx, val in enumerate(restecg_map)})

# Convert 'slope' (slope of the peak exercise ST segment)
df['slope'] = df['slope'].map({0: 'upsloping', 1: 'flat', 2: 'downsloping'})

# Convert 'thal' (thalassemia)
thal_map = {1: 'normal', 2: 'fixed defect', 3: 'reversible defect'}
df['thal'] = df['thal'].map({val: idx for idx, val in enumerate(thal_map)})

# You can also use one-hot encoding for categorical features
df = pd.get_dummies(df, columns=['cp', 'restecg', 'slope', 'thal'], drop_first=True)

# Define age groups
age_bins = [29, 40, 50, 60, 70, 80]
age_labels = ['30-40', '40-50', '50-60', '60-70', '70-80']

# Create a new feature 'age_group'
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

# Convert 'age_group' into a numerical feature
age_group_map = {label: idx for idx, label in enumerate(age_labels)}
df['age_group'] = df['age_group'].map(age_group_map)

# Check the new 'age_group' feature
print(df[['age', 'age_group']].head())

# Remove outliers for 'chol' (values beyond 3 standard deviations)
chol_mean = df['chol'].mean()
chol_std = df['chol'].std()
df = df[df['chol'] < chol_mean + 3*chol_std]
df = df[df['chol'] > chol_mean - 3*chol_std]

# Cap values for 'trestbps' to the 1st and 99th percentiles
lower, upper = df['trestbps'].quantile([0.01, 0.99])
df['trestbps'] = df['trestbps'].clip(lower, upper)

# Scale the numeric features (e.g., 'age', 'trestbps', 'chol')
scaler = StandardScaler()
df[['age', 'trestbps', 'chol']] = scaler.fit_transform(df[['age', 'trestbps', 'chol']])

# Handle missing values with SimpleImputer (impute with mean)
imputer = SimpleImputer(strategy='mean')
df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Define X (features) and y (target)
X = df.drop(columns=['target'])
y = df['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression(max_iter=10000)  # Adding max_iter to avoid convergence issues
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print("Classification Report:\n", classification_report(y_test, y_pred))