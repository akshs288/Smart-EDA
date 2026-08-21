import streamlit as st
import numpy as np


st.subheader("📊Statistical Analysis")

if "df" in st.session_state:
    df = st.session_state["df"]

    col_name = df.select_dtypes(include="number").columns
    col_name_lst = list(col_name)

    new_lst = []
    if len(col_name) > 2:
        for i in col_name_lst:
            if ("id" in i.lower()):
                continue
            else:
                new_lst.append(i)                

        new_df = df[new_lst].copy()
        new_df = new_df.fillna(new_df.mean())
        corr_matrix = new_df[new_lst].corr()

        st.subheader("🎯Correlation Matrix")
        
        upper = corr_matrix.where(
        np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
        # Strongest positive
        max_pair = upper.stack().idxmax()
        max_value = upper.stack().max()

        # Strongest negative
        min_pair = upper.stack().idxmin()
        min_value = upper.stack().min()
        
        highest_corr = f"{max_pair[0]} <-> {max_pair[1]} = {max_value}"
        st.metric(f"📈Highest Correlation:",highest_corr,border=True)
        
        lowest_corr = f"{min_pair[0]} <-> {min_pair[1]} = {min_value}"
        st.metric(f"📉Lowest Correlation:",lowest_corr,border=True)
        
        
    else:
        st.error("This data does not fit to show correlation and covariance tables.")
