# Wine Quality Classification with Ensemble Machine Learning

**Author:** Mhamed  
**Date:** 04, 10, 2025 

## Objective

This project aims to classify red wine quality based on its physicochemical properties using Random Forest and Gradient Boosting machine learning models. Original quality scores (0–10) are grouped into:

- **Low (0)**: Score ≤ 4  
- **Medium (1)**: Score 5–6  
- **High (2)**: Score ≥ 7  

This simplifies the task into **multi-class classification**, enabling more effective model training and interpretation.---

## Dataset

- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality)
- **Name**: Wine Quality – Red
- **Samples**: 1,599 red wine samples
- **Features**: 11 numeric chemical attributes (e.g., alcohol, pH, citric acid)
- **Target**: Wine quality (transformed to 0, 1, 2)

## Methodology

### 1. Data Preparation
- Loaded dataset and inspected structure
- Created `quality_label` (text) and `quality_numeric` (0,1,2) columns
- Removed original quality columns from features

### 2. Feature Selection
- Selected all chemical properties as predictors (X)
- Target variable: `quality_numeric` (y)

### 3. Data Splitting
- Used `train_test_split` with stratification (80% train / 20% test)

### 4. Models Implemented
- Random Forest (100 estimators)
- Gradient Boosting (100 estimators)

### 5. Evaluation Metrics
- **Accuracy**
- **F1 Score (Weighted)**
- **Confusion Matrix**
- **Generalization Gaps** (Train vs Test Performance)

## Model Evaluation Function

## Compare Results

## Conclusion and Insights



## Windows Setup Instructions

Open a PowerShell terminal in VS Code. 
Create local project virtual environment, activate it, and install packages. 
When asked to use the new .venv click yes. 


```shell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install -r requirements.txt
py -m pip install -r requirements.txt

Push the final work to GitHub repo.

```shell
git add .
git commit -m "describe the change here"
git push -u origin main
```

For additional information and suggestions, follow the process for professional Project Setup / Initialization / Standard Workflow in
[pro-analytics-01](https://github.com/denisecase/pro-analytics-01)

## Dataset Source

The Wine Quality Dataset is made available by the UCI Machine Learning Repository..

[https://archive.ics.uci.edu/ml/datasets/Wine+Quality](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)