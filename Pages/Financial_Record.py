import streamlit as st
import pandas as pd

st.subheader("📈Numerical Analysis")

if "df" in st.session_state:
    df = st.session_state["df"]
    summary_data = df.describe()
    st.write(summary_data)

    st.subheader("Categorical Summary")
    



