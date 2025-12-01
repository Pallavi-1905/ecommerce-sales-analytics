📊 E-commerce Sales Analytics Project (Enhanced)

A complete end-to-end Data Analytics & ML project using a realistic synthetic e-commerce sales dataset (2000+ records).
Includes data cleaning, EDA, visualizations, feature engineering, ML forecasting, and an optional Streamlit dashboard.

🗂️ Project Structure
ecommerce-sales-analytics/
│── data_cleaning.py
│── visualizations.py
│── model_training.py
│── main.ipynb
│── sales.csv
│── requirements.txt
│── README.md

📌 Project Overview

This project analyzes sales performance from a simulated e-commerce store to discover:

Revenue trends

Customer purchasing behavior

Product performance

Seasonality & monthly patterns

Predictive sales insights

It follows a clean Analytics → Visualization → ML Forecasting pipeline.

🧹 1. Data Cleaning

Performed in data_cleaning.py:

✔ Removed duplicates
✔ Handled missing values
✔ Standardized date formats
✔ Created new features:

Month

Quarter

Revenue

Year

Profit

✔ Exported clean dataset for analysis

📈 2. Exploratory Data Analysis (EDA)

Performed using Pandas, NumPy & Matplotlib/Seaborn.

Key insights extracted:

Top-selling products

Revenue contribution by category

Region-wise customer demand

Monthly & yearly sales performance

Customer order frequency

Average order value trends

Visuals generated include:

Bar charts

Line charts

Heatmaps

Category Comparisons

Monthly trends

Profit vs Revenue analysis

All charts are generated in visualizations.py.

🤖 3. Machine Learning Model

Model training workflow in model_training.py:

Feature selection

Train-test split

Standardization

Trained models tried:

Linear Regression

Random Forest Regressor

Evaluated using:

MAE

MSE

R² Score

Best model saved for future predictions.

🧪 4. Jupyter Notebook (main.ipynb)

This notebook contains:

Full EDA in one place

Graphs rendered interactively

Model evaluation

Summary insights

Perfect for recruiters to view your analysis.

🖥️ 5. Optional: Streamlit Dashboard

A simple interactive dashboard (if you want to add):

View KPIs: Total Revenue, Avg Order Value, Total Profit

Select product categories

View filtered sales charts

Upload your own CSV

View monthly sales trends

You can create app.py later if needed.

📊 Key Insights (Sample)

Electronics category generates the highest revenue.

North region drives 40–45% of total sales.

Revenue shows strong seasonal spikes during Q3.

Average order value is steadily increasing YoY.

ML model predicts an upward trend for next month’s sales.

🛠️ Technologies Used
Area	Tools
Programming	Python
Data Processing	Pandas, NumPy
Visualizations	Matplotlib, Seaborn
Machine Learning	scikit-learn
Dashboard	Streamlit
Notebook	JupyterLab / Jupyter Notebook
▶️ How to Run the Project
1. Clone Repository
git clone https://github.com/yourusername/ecommerce-sales-analytics.git
cd ecommerce-sales-analytics

2. Install Dependencies
pip install -r requirements.txt

3. Run Data Cleaning
python data_cleaning.py

4. Run Visualizations
python visualizations.py

5. Train Model
python model_training.py

6. (Optional) Launch Dashboard
streamlit run app.py

📚 Future Improvements

Customer segmentation (K-means clustering)

Product recommendation system

Add SQL integration

Deploy Streamlit app online

Create Power BI dashboard

📥 Dataset

sales.csv is a realistic, high-quality synthetic dataset with:

2000+ records

10+ useful features

Multiple product categories

Realistic order timestamps

Revenue & profit values
