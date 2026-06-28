# Executive Retail & Financial Analytics Platform

An interactive data visualization application built using Python, Streamlit, and Plotly. The application connects directly to an analytical MySQL database layer to dynamically render business performance metrics and real-time financial tracking indices.

## Tech Stack & Skills Highlighted
- **Frontend Dashboarding:** Python `streamlit` (Layout design, state rendering, reactive widgets)
- **Data Visualization:** `Plotly Express` (Interactive, dark-themed metric graphing)
- **Database Querying:** `pandas.read_sql()` combined with `SQLAlchemy` relational schema joins

## System Functionality
1. **Dynamic Data Fetching:** Directly triggers SQL queries against local analytical databases rather than caching static configurations.
2. **Relational Table Joining:** Merges operational transactions (`fct_orders`) with dimension properties (`dim_customers`) on-the-fly.
3. **Dual Metric Tracking:** Visually tracks corporate sales statistics next to live global currency indicators.
