import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.title("Smart EDA 📊")
file = st.file_uploader("📁 Upload file to extract meaningful insights")

if file:
    df = pd.read_csv(file)
    row,col = tuple(df.shape)

    col1,col2 = st.columns(2)
    with col1:
        st.metric("↔️Number of Rows in a data:",row,border=True)

    with col2:
        st.metric("↕️Number of Columns in a data:",col,border=True,)
    
    null_data = df.isnull().sum().astype(int).to_dict()

    print(null_data)
    st.subheader("📑Missing values in Data")
    new_null_df = pd.DataFrame(null_data,index=[0])
    st.write(new_null_df)
    
    # Calculating percentages of missing value in data for particular column
    col_names = list(new_null_df.columns)
    d = {}    
    
    null_values = list(df.isnull().sum().astype(int))
    print(null_values)
    for i in range(len(col_names)):
        percent_col = ((null_values[i]/row)*100)
        rounded_percentage = round(percent_col,4)
        d[col_names[i]] = str(rounded_percentage)+"%"
    
    st.subheader("❓Missing Values in percentage")
    df_percent_missing = pd.DataFrame(d,index=[0])
    st.write(df_percent_missing)
    
    # Display Data types of objects
    d1 = dict(df.dtypes)
    new_dtype = pd.DataFrame(d1,index=[0])
    st.subheader("🔢Data types of different columns")
    st.write(new_dtype)

    # Displaying duplicate rows
    st.subheader("👥Duplicate Records")
    duplicate_rec = df[df.duplicated()]
    st.write(duplicate_rec)
    
    # Creating Bar graph for null values for better understanding.
    st.subheader("📊Bar Graph for Null Values")
    bar_data = pd.DataFrame({
        "Columns":col_names,
        "Null Values":null_values
    })
    bar_graph = px.bar(bar_data,x="Columns",y="Null Values")
    st.plotly_chart(bar_graph)
    
    
    # st.subheader("📄Handeling Missing Values")
    

