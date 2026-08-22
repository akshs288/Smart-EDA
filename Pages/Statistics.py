import streamlit as st
import numpy as np
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

        new_df = df[new_lst].copy()
        new_df = new_df.fillna(new_df.mean())
        corr_matrix = new_df[new_lst].corr()

        st.subheader("🎯Correlation Insights")
        
        upper = corr_matrix.where(
        np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
        # Strongest positive
        max_pair = upper.stack().idxmax()
        max_value = upper.stack().max()

        # Strongest negative
        min_pair = upper.stack().idxmin()
        min_value = upper.stack().min()
        
        highest_corr = f"{max_pair[0]} <-> {max_pair[1]} = {round(max_value,3)}"
        st.metric(f"📈Highest Correlation:",highest_corr,border=True)
        
        lowest_corr = f"{min_pair[0]} <-> {min_pair[1]} = {round(min_value,3)}"
        st.metric(f"📉Lowest Correlation:",lowest_corr,border=True)
    
    else:
        st.error("This data does not fit to show correlation and covariance tables.")

    # Outlier detection
    def outlier():
        d=df.select_dtypes(include="number")
        l = list(d.columns)
        for i in l:
            if "id" in i.lower():
                continue
            else:
                l_name = []
                upper_l = []
                lower_l = []
                outliers_l = []
                for i in l:
                    if "id" in i.lower():
                        continue
                
                    else:
                        l_name.append(i)
                        q1 = df[i].quantile(0.25)
                        q3 = df[i].quantile(0.75)
                        iqr = q3-q1
                        lower_fence = round(float(q1-(1.5*iqr)),2)
                        upper_fence = round(float(q3+(1.5*iqr)),2)
                        upper_l.append(upper_fence)
                        lower_l.append(lower_fence)

                        outliers = []
                        for j in d[i]:
                            if (j > upper_fence) or (j < lower_fence):
                                outliers.append(j)
                        outliers_l.append(len(outliers))

        result = {}
        result["Columns"] = l_name
        result["Upper Fence"] = upper_l
        result["Lower Fence"] = lower_l
        result["Outliers"] = outliers_l
        st.write("Outlier Matrix")

        st.dataframe(result)
            
    
    outlier()
