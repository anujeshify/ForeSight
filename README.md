# **ForeSight: Advanced Retail Analytics Platform**

ForeSight is an advanced retail analytics platform that combines sentiment analysis, statistical sales analysis, and demand forecasting to provide actionable insights. It empowers businesses to understand customer behavior and make strategic decisions for growth and efficiency.

## **Table of Contents**

- [Introduction](#introduction)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Data](#data)
- [Modules](#modules)
- [Outputs](#outputs)
- [Authors](#authors)

---

## **Introduction**

ForeSight is designed to provide comprehensive insights into sales trends and customer sentiment using a combination of data analysis techniques, sentiment analysis, and demand forecasting models. By leveraging advanced analytics, businesses can gain valuable insights to drive efficiency, enhance customer experiences, and optimize their strategies.

## **Features**

- **Sentiment Analysis:** Understand customer reviews and sentiments towards products, allowing for more effective product management.
- **Statistical Sales Analysis:** Gain insights into sales trends, patterns, and product performance over time.
- **Demand Forecasting:** Utilize advanced forecasting techniques to predict future sales demand, helping businesses plan inventory and sales strategies.
- **User-Friendly Interface:** Interactive dashboard built with Streamlit for easy navigation and insights visualization.

---

## **Folder Structure**

The repository is organized as follows:

```
ForeSight/
│
├── Views/
│   ├── category_analysis.py
│   ├── demand_forecasting.py
│   ├── homepage.py
│   └── summary.py
│
├── Assets/
│   └── [Files used for the Streamlit website, including the ForeSight logo]
│
├── Jupyter/
│   └── Walmart_Sparkathon_Reviews_Sentiment_Analysis.ipynb
│
├── Datasets/
│   └── product_sales_reviews_diverse.csv
│
├── app.py
├── forecasting_arima.ipynb
├── README.md
└── requirements.txt
```

- **Views**: Contains Python scripts responsible for different pages of the Streamlit application.
- **Assets**: Includes all the assets such as logos and images used for the web application.
- **Jupyter**: Contains the Jupyter Notebook used for initial analysis and sentiment analysis.
- **Datasets**: Contains the CSV files used for testing and simulation.

---

## **Installation**

To set up the application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/anujeshify/ForeSight.git
   ```
2. Navigate to the directory:
   ```bash
   cd ForeSight
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Running the Application**

To run the application, use the following command:

```bash
streamlit run app.py
```

The Streamlit application will launch, and you can access it via your web browser at `http://localhost:8501`.

---

## **Data**

The dataset `product_sales_reviews_diverse.csv` used in this project is created for simulation purposes and contains manually curated data for product reviews, sales, and other related attributes. The data is used to simulate a real-world scenario to demonstrate the platform's capabilities.

---

## **Modules**

### **Views**

- `category_analysis.py`: Contains code for analyzing product categories and their performance.
- `demand_forecasting.py`: Implements demand forecasting models to predict future sales.
- `homepage.py`: The main homepage script for the Streamlit application.
- `summary.py`: Provides a summary of key insights from the analysis.

### **Jupyter Notebooks**

- **Walmart_Sparkathon_Reviews_Sentiment_Analysis.ipynb**: Initial exploratory data analysis and sentiment analysis using reviews data.

### **Main Application Script**

- `app.py`: The main script to run the Streamlit application.

---

## **Outputs**

The outputs of the ForeSight platform are displayed in an interactive dashboard with the following key insights:

- **Sentiment Analysis**: Graphs and visualizations showcasing customer sentiment towards products.
- **Sales Analysis**: Insights into sales trends, including best-selling products, seasonal trends, and category-wise performance.
- **Demand Forecasting**: Forecasted sales trends displayed as graphs to help businesses plan inventory and marketing strategies.

These insights are presented through an easy-to-navigate interface, enabling users to drill down into details for strategic decision-making.

---

## **Authors**

- **Anujesh Bansal** - anujeshify[https://github.com/anujeshify]
- **Divyansh Chauhan** - DivR22[https://github.com/DivR22]
- **Khushi Goel** - Khushigoel14[https://github.com/Khushigoel14]
- **Prachee Mohapatra** - prachee04[https://github.com/prachee04]

