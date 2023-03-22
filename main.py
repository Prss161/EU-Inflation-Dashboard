import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Inflation in EU',
                   page_icon = 'bar_chart:',
                   layout = 'wide')
df = pd.read_excel(
    io = 'Data.xlsx',
    engine ='openpyxl',
    sheet_name = 'Arkusz1',
    usecols = 'A:AW',
    nrows = 1000,
)

st.dataframe(df)