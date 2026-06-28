import streamlit as st
import pandas as pd
import sqlalchemy
import plotly.express as px

st.set_page_config(page_title="Zambian Retail & Financial Analytics", layout="wide")
st.title("Executive Retail & Currency Analytics Platform")
st.markdown("This dashboard updates automatically by querying your live local MySQL database layer.")

# DATABASE CONNECTIVITY LAYER
db_username = 'root'
db_password = 'darry@2005'
db_name = 'retail_analytics'

connection_url = sqlalchemy.engine.URL.create(
    drivername="mysql+mysqlconnector",
    username=db_username,
    password=db_password,
    host="127.0.0.1",
    port=3306,
    database=db_name
)
engine = sqlalchemy.create_engine(connection_url)

# DATA EXTRACTION LAYER (SQL Queries)
try:
    # Querying retail transaction records
    orders_df = pd.read_sql("SELECT * FROM fct_orders", con=engine)
    customers_df = pd.read_sql("SELECT * FROM dim_customers", con=engine)
    
    # Querying live currency metrics
    currency_df = pd.read_sql("SELECT * FROM dim_currency_rates", con=engine)
    
    # Merge customer dimensions with fact files for rich charts
    full_retail_df = orders_df.merge(customers_df, on='CustomerID')

    # DASHBOARD VISUALIZATION DESIGN
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Total Sales Revenue by Item")
        # Aggregate revenue by products using pandas
        sales_summary = full_retail_df.groupby('Item_Details')['Price_Paid'].sum().reset_index()
        
        # Building an interactive Plotly bar chart
        fig_sales = px.bar(sales_summary, x='Item_Details', y='Price_Paid', 
                           labels={'Price_Paid':'Total Revenue (ZMW)', 'Item_Details':'Product Name'},
                           color='Item_Details', template="plotly_dark")
        st.plotly_chart(fig_sales, use_container_width=True)

    with col2:
        st.subheader("Live Global Exchange Values (Per 1 USD)")
        # Building an interactive Plotly horizontal bar chart for currency indicators
        fig_currency = px.bar(currency_df, x='Exchange_Rate', y='Currency_Code', 
                              orientation='h', labels={'Exchange_Rate':'Value relative to USD', 'Currency_Code':'Currency'},
                              color='Currency_Code', template="plotly_dark")
        st.plotly_chart(fig_currency, use_container_width=True)
        
    # Bottom Layout: Detailed Operational View Tables
    st.subheader("Live Analytical Database Ledger Views")
    show_col1, show_col2 = st.columns(2)
    with show_col1:
        st.write("Clean Orders Table (`fct_orders`)", orders_df)
    with show_col2:
        st.write("Live Exchange Index (`dim_currency_rates`)", currency_df)

except Exception as e:
    st.error(f"Failed to connect to MySQL database: {e}")
    st.info("Ensure your MySQL Server is running and populated before executing the dashboard platform.")

