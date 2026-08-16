import streamlit as st
import pandas as pd

st.subheader("📈Numerical Analysis")

if "df" in st.session_state:
    df = st.session_state["df"]
    summary_data = df.describe()
    st.write(summary_data)

    st.subheader("📊Categorical Summary")
    
    cola,colb= st.columns(2)

    list_names = list(df.select_dtypes(include=["object", "string", "category"]).columns)  # All columns which have object type.
    with cola:
        first_col_name = list_names[1]
        max_occ = df[first_col_name].mode()[0]

        st.metric(f"🔁Most Frequent '{first_col_name}' value",max_occ,border=True)

    with colb:
        first_col_name2 = list_names[2]
        min_occ = df[first_col_name2].value_counts().sort_values(ascending=False).iloc[2]
        st.metric(f"🔁Least Frequent '{first_col_name2}' value",min_occ,border=True)

    st.subheader("🧮Frequency Table")
    main_d = {}
    
    c = 0
    for i in list_names:
        c+=1
        val_fre_dict = {}
        total_values = df[i].value_counts()
        index_ = list(total_values.index[:5])
        val_ = [int(i) for i in total_values.values[:5]]
        val_fre_dict["🔢Values"] = index_
        val_fre_dict["🎯Frequency"] = val_
        main_d[i] = val_fre_dict

    for j in main_d:
        st.write(j)
        result_df = pd.DataFrame(main_d[j])
        st.write(result_df)

    
    
    
    
    