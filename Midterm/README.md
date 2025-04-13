# Lab 4 – Predicting a Continuous Target with Regression (Titanic)
**Author:** Mhamed  
**Date:** 04, 04, 2025 
 
## Introduction
In this lab, we will apply regression models to predict passenger fares using the Titanic dataset. We will explore and prepare the data, train a basic Linear Regression model, and compare it with advanced models like Ridge, Elastic Net, and Polynomial Regression. The goal is to evaluate model performance, handle overfitting, and understand how different features and regularization techniques affect predictions.

## Section 1. Import and Inspect the Data
   - Load the dataset and display the first 10 rows.

## Section 2. Data Exploration and Preparation
   - Prepare the Titanic data for regression modeling
   
## Section 3. Feature Selection and Justification
   - Case 1. age only
      X1 = titanic[['age']]
      y1 = titanic['fare']
   - Case 2. family_size only
      X2 = titanic[['family_size']]
      y2 = titanic['fare']
   - Case 3. age and family size
      X3 = titanic[['age', 'family_size']]
      y3 = titanic['fare']
   - Case 4. age and pclass
      X4 = titanic[['age', 'pclass']]
      y4 = titanic['fare']
   - Reflection
## Section 4. Train a Regression Model (Linear Regression)
   - Split the Data
   - Train and Evaluate Linear Regression Models (all 4 cases)
   - Report Performance
   - Reflection
## Section 5. Compare Alternative Models
   - Ridge Regression (L2 penalty)
   - Elastic Net (L1 + L2 Combined)
   - Polynomial Regression
   - Visualize Polynomial Cubic Fit (for 1 input feature)
   - Reflections on Polynomial Fit
   - Compare All Models
   - Visualize Higher Order Polynomial (for the same 1 input case)
   - Reflection
## Section 6. Final Thoughts & Insights
   - Summarize Findings
   - Discuss Challenges