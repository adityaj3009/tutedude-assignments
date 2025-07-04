# 🦠 COVID-19 Data Analysis Project

This project is part of Module 12 of the Data Science course and involves analyzing the impact of COVID-19 in different countries and comparing it with happiness metrics.

## 📁 Datasets Used

- `covid19_Confirmed_dataset.csv`: Time series data of confirmed COVID-19 cases worldwide.
- `worldwide_happiness_report.csv`: Dataset containing happiness indicators like GDP per capita, social support, life expectancy, and freedom.

## 📊 Objective

To explore relationships between COVID-19 maximum infection rates and the following happiness indicators:

- GDP per capita
- Social support
- Healthy life expectancy
- Freedom to make life choices

## 📌 Key Tasks

- Preprocessing and cleaning both datasets.
- Aggregating COVID-19 data by country.
- Calculating maximum daily infection rates.
- Merging the two datasets on country names.
- Performing correlation analysis.
- Creating scatter plots and regression plots to visualize trends.

## 📈 Visualizations

All visualizations were done using `Seaborn` and `Matplotlib`, including:

- Max infection rate vs. GDP per capita (with `log` transformation : np.log() )
- Max infection rate vs. Social support
- Max infection rate vs. Life expectancy
- Max infection rate vs. Freedom to make life choices

## 🔍 Insights

- Countries with **higher GDP per capita** generally had **lower max infection rates** (moderate negative correlation).
- **Social support** and **life expectancy** showed some correlation with infection spread.
- No strong correlation was found between **freedom to make life choices** and COVID-19 impact.

## 🛠️ Technologies Used

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Jupyter Notebook
- VS code
