import streamlit as st
import pandas as pd

st.subheader("📈Numerical Analysis")

if "df" in st.session_state:
    df = st.session_state["df"]
    summary_data = df.describe()
    st.write(summary_data)

    st.subheader("Categorical Summary")
    
    cola,colb= st.columns(2)

    with cola:
        list_names = df.select_dtypes(include=["object"]).columns
        first_col_name = list_names[1]
        max_occ = df[first_col_name].mode()[0]

        st.metric(f"🔁Most Frequent '{first_col_name}' value",max_occ,border=True)



