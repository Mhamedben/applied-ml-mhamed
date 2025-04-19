# Final Project: Predicting Medical Insurance Charges with Regression Analysis - Mhamed  

**Author:** Mhamed  
**Date:** 04, 15, 2025 


## Project Files:
* [Dataset: insurance.csv] (https://github.com/Mhamedben/applied-ml-mhamed/blob/main/ML_RegressionMM/Data/insurance.csv)

* [Jupyter Notebook: Regression_Project_Mhamed.ipynb] (https://github.com/Mhamedben/applied-ml-mhamed/blob/main/ML_RegressionMM/Regression_Project_Mhamed.ipynb)

* [Peer Review: peer_review.md] (https://github.com/ericmeyer1/ml_regression_eric/blob/main/ml_regression_eric.ipynb)

## Instructions on how to set up your virtual environment and run your notebook locally:

To run this notebook on your own computer: 
1. Clone the Repository:

git clone https://github.com/Mhamedben/applied-ml-mhamed/blob/main/ML_RegressionMM/REGRESSION_PROJECT_Mhamed.ipynb.md

2. Create a Virtual Environment:
python -m venv .venv

3. Activate the Virtual Environment:
For windows: .\.venv\Scripts\activate
On macOS/Linux: .venv/bin/activate
 
## Introduction
This project focuses on predicting individual medical insurance charges using demographic and health-related factors like age, BMI, number of children, smoking status, and region. Using the Medical Cost Personal Dataset, we’ll explore the data, preprocess it, and build regression models through a streamlined machine learning pipeline.

## Section 1. Import and Inspect the Data
   - Load the dataset and display the first 10 rows.
   - Check for missing values and display summary statistics
   - Reflection 1:  What do you notice about the dataset? Are there any data issues?
  
## Section 2. Data Exploration and Preparation
   - Explore data patterns and distributions
   - Create histograms, boxplots, and count plots for categorical variables
   - Handle missing values and clean data
   - Feature selection and engineering
   - Correlation heatmap to explore feature relationships
   - Reflection 2: What patterns or anomalies do you see? Do any features stand out? What preprocessing steps were necessary to clean and improve the data? Did you create or modify any features to improve performance?
   
## Section 3. Feature Selection and Justification
   - Choose Features and Target
   - Define X and y
   - Reflection 3: Why did you choose these features? How might they impact predictions or accuracy?

## Section 4. Train a Model (Linear Regression)
   - Split the data into training and test sets using train_test_split
   - Train model using Scikit-Learn model.fit() method.
   - Evaluate Performance
   - Reflection 4: How well did the model perform? Any surprises in the results?

## Section 5. Improve the Model or Try Alternates (Implement Pipelines)
   - Implement Pipeline 1: Imputer → StandardScaler → Linear Regression.
   - Implement Pipeline 2: Imputer → Polynomial Features (degree=3) → StandardScaler → Linear Regression.
   - Compare performance of all models across the same performance metrics
   - Reflection 5: Which models performed better? How does scaling impact results?

## Section 6. Final Thoughts & Insights
   - Summarize Findings
   - Discuss Challenges faced
   - Reflection 6: What did you learn from this project?