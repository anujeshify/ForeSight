import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sales_data = pd.read_csv("Datasets/test_dataset_1.csv")

sentiment_data = pd.read_csv("Datasets/category_avg_net_sentiments.csv")

category_sales = sales_data.groupby('Category')['TotalSales'].sum().reset_index()
category_sales = category_sales.sort_values(by='TotalSales', ascending=False)
category_sales['Rank by Total Sales'] = range(1, len(category_sales) + 1)

sentiment_data = sentiment_data.merge(category_sales[['Category', 'Rank by Total Sales']], on='Category')

st.sidebar.title("Walmart Product Analysis")
categories = sales_data['Category'].unique()
selected_category = st.sidebar.selectbox("Choose Category", categories)


st.header("Category Analysis")
grouped_stats = sales_data.groupby(['Category', 'ProductName']).agg(
    TotalSales_Median=('TotalSales', 'median'),
    TotalSales_Sum=('TotalSales', 'sum'),
    TotalSales_Min=('TotalSales', 'min'),
    TotalSales_Max=('TotalSales', 'max')
).reset_index()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.header("Total Sales Median")
    st.write(grouped_stats['TotalSales_Median'].mean())
with col2:
    st.header("Total Sales Sum")
    st.write(grouped_stats['TotalSales_Sum'].sum())
with col3:
    st.header("Total Sales Min")
    st.write(grouped_stats['TotalSales_Min'].min())
with col4:
    st.header("Total Sales Max")
    st.write(grouped_stats['TotalSales_Max'].max())


col1, col2 = st.columns(2)
with col1:
    top_categories = sales_data.groupby('Category')['TotalSales'].sum().nlargest(5)
    fig, ax = plt.subplots()
    colors = sns.color_palette("husl", len(top_categories))
    sns.barplot(x=top_categories.values, y=top_categories.index, ax=ax, palette=colors)
    ax.set_xlabel('Total Sales')
    ax.set_ylabel('Category')
    ax.set_title('Top 5 Categories by Sales')
    st.pyplot(fig)

with col2:
    st.write("Top 5 Categories by Sentiment")

    top_5_sentiment = sentiment_data.sort_values(by='SentimentScore1_10', ascending=False).head(5)

    top_5_sentiment_display = top_5_sentiment[['Category', 'SentimentScore1_10', 'Rank by Total Sales']]
    st.dataframe(top_5_sentiment_display, width=2000, height=210, use_container_width=True)


if st.sidebar.button("Show Analysis"):
    st.header(f"Analysis for {selected_category}")
    st.write("Description to be added later...")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("basic stats")

    with col2:
        st.write("data frame with values")
