# 📊 Employee Performance and Retention Analysis

**🗓️ Date**: July 7, 2025  
**📁 Project**: Predictive Analysis of Employee Performance and Attrition using Machine Learning and Deep Learning  
**👨‍💻 Tools & Libraries**: `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`, `Scikit-learn`, `TensorFlow/Keras`

---

## 🚀 **Objective**

This project focuses on analyzing and predicting employee performance and attrition based on real-world HR data. The aim is to apply concepts from **Probability**, **Statistics**, **Machine Learning**, and **Deep Learning** to identify trends and build predictive models for HR decision-making.

---

## 🧰 **Libraries Used**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, r2_score, mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
```
---

## 📌 **Phase 1 - Data Collection and Exploratory Data Analysis (EDA)**

### ✅ **Step 1 - Data Collection and Preprocessing**
- **Dataset**: `Employee_data.csv`
- **Initial Features**:
  - Employee ID  
  - Name  
  - Age  
  - Department  
  - Salary  
  - Years at Company  
  - Performance Score  
  - Attrition (Yes/No)
- **Preprocessing Tasks**:
  - Loaded dataset using `pandas`
  - Checked for and removed **duplicate rows**
  - Handled **missing values** using appropriate imputation
  - Cleaned **inconsistent entries** (e.g., salary formats, spelling mismatches)
  - Verified column data types for modeling

---

### ✅ **Step 2 - Exploratory Data Analysis (EDA)**
- **Descriptive Statistics**:
  - Used `.describe()` for summary stats (mean, std, min, max)
  - Calculated **median**, **mode**, **variance** manually
- **Data Visualizations**:
  - `sns.pairplot()` to examine inter-feature relationships
  - `sns.heatmap()` to explore **correlation matrix**
  - `sns.boxplot()` to detect **outliers** in Age, Salary, Performance Score

---

### ✅ **Step 3 - Probability and Statistical Analysis**
- **Probability**:
  - Estimated P(Attrition = Yes | Department = Sales)
  - Calculated conditional probabilities based on department and performance levels
- **Bayes' Theorem**:
  - Applied to calculate P(Attrition | Low Performance)
- **Hypothesis Testing**:
  - Null Hypothesis: Mean Performance Score is the same across all departments
  - Performed **ANOVA test**
  - Interpreted p-value and test statistic to reject or accept the null

---

## 📌 **Phase 2 - Predictive Modeling**

### ✅ **Step 4 - Feature Engineering and Encoding**
- **Scaling**:
  - Applied `StandardScaler` to numerical features: Salary, Performance Score
- **Encoding**:
  - Applied `LabelEncoder` to categorical features:
    - Department (e.g., HR, Tech, Sales)
    - Attrition (Yes = 1, No = 0)
- **Outcome**:
  - Final feature matrix ready for training models

---

### ✅ **Step 5 - Employee Attrition Prediction Model**
- **Model**: Logistic Regression (`sklearn.linear_model.LogisticRegression`)
- **Input Features**:
  - Age, Department (encoded), Salary, Performance Score, Years at Company
- **Target**: Attrition (1 = Yes, 0 = No)
- **Process**:
  - Data split into 80% training and 20% testing sets
  - Model trained using training set
  - Predictions made on test set
- **Evaluation Metrics**:
  - **Accuracy Score**
  - **Precision Score**
  - **Recall Score**
  - **F1-Score**
  - **Confusion Matrix** (visualized using `sns.heatmap()`)

---
### ✅ **Step 6 - Employee Performance Prediction Model**
- **Model Used**: Linear Regression
- **Goal**: Predict numeric performance score
- **Evaluation Metrics**:
  - **R-squared (R²)**
  - **Mean Squared Error (MSE)**
- **Visualizations**:
  - **Scatter plot** of predicted vs actual performance scores

---

## 📌 **Phase 3 - Deep Learning Models**

### ✅ **Step 7 - Deep Learning for Employee Performance Prediction**
- **Framework Used**: TensorFlow / Keras
- **Neural Network Architecture**:
  - **Input Layer**: Features like Age, Salary, Department
  - **Hidden Layers**: Dense layers with ReLU activation
  - **Output Layer**: Predicted Performance Score (regression output)
- **Loss Function**: Mean Squared Error
- **Evaluation**:
  - Performance on test set compared to baseline models

---

### ✅ **Step 8 - Deep Learning for Employee Attrition Classification**
- **Goal**: Predict if employee will leave (Yes/No)
- **Input Features**: Age, Department, Performance Score, Salary, Years at Company
- **Model**:
  - **Binary Classification** with sigmoid output
- **Evaluation Metrics**:
  - Accuracy
  - Precision
  - Recall
  - F1-score

---

## 📌 **Phase 4 - Reporting and Insights**

### ✅ **Step 9 - Insights and Recommendations**

#### 🔍 **Key Findings**
- **Performance Factors**:
  - Higher salary and tenure are positively correlated with performance
- **Attrition Risks**:
  - Lower performance and certain departments show higher attrition

---

### ✅ **Step 10 - Data Visualization and Reporting**

#### 📊 **Visuals Generated**:
- **Line Plots**: Performance trends over time
- **Bar Charts**: Attrition by department
- **Scatter Plots**: Salary vs Performance Score

---

## ✅ **Submission Checklist**

- [x] **Jupyter Notebook, google collab**: `employee.ipynb`
- [x] **Data Visualizations**: Included in the notebook 
- [x] **Final Report**: ALL information in employee.md

---

## 🎯 **Learning Outcomes**

- Importance of data preprocessing and cleaning
- Basics of probability and hypothesis testing in HR analytics
- Model building using both **ML (Logistic & Linear Regression)** 
- Extracting real-world HR insights from raw data

---

## 📂 **Dataset Information**

- **Source**: `Employee_data.csv`  
- **Contains**: Personal and job-related features such as:
  - Age, Department, Years at Company, Salary, Attrition, Performance Score

---




