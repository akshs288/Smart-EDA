import pandas as pd
import numpy as np
import plotly
import streamlit as st
import matplotlib.pyplot as plt

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

    st.subheader("📑Missing values in Data")
    new_null_df = pd.DataFrame(null_data,index=[0])
    st.write(new_null_df)
    
    # Calculating percentages of missing value in data for particular column
        
    
    
    
    
    # Time to Display Data types of objects
    d1 = dict(df.dtypes)
    new_dtype = pd.DataFrame(d1,index=[0])
    st.subheader("🔢Data types of different columns")
    st.write(new_dtype)
    
    
    # st.subheader("📄Handeling Missing Values")
    

