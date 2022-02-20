import streamlit as st
import pandas as pd
import json
from io import StringIO

st.title("PrismForce.ai")

file = st.file_uploader("Pick a file")

if st.button("Analyse"):
    if file is not None:
        #taking input as string
        stringio = StringIO(file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        #converting to json
        data = json.loads(string_data)

        expense = pd.DataFrame.from_dict(data['expenseData'])
        revenue = pd.DataFrame.from_dict(data['revenueData'])
        #st.write(expense)
        #st.write(revenue)
        result = pd.merge(revenue,expense,how='outer',on="startDate")
        result.fillna(0,inplace=True)
        result["amount"] = result["amount_x"]-result["amount_y"]
        result = result.groupby("startDate").sum()
        result = result.drop(["amount_x","amount_y"],axis = 1)
        result.reset_index(inplace=True)
        st.write("Balance Sheet:")
        st.write(result)
        