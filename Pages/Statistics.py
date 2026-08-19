import streamlit as st
import pandas as pd

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

        df[new_lst] = df[new_lst].fillna(df[new_lst].mean())
        corr_matrix = df[new_lst].corr()
        print(corr_matrix)
        

    else:
        st.error("This data does not fit to show correlation and covariance tables.")




