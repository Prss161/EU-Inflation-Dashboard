import pandas as pd
import plotly.express as px
import streamlit as st

#Need to think about scraping data from website eu statista with panda.

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

#Transposing data table
df = df.T
df.columns = df.iloc[0]
df = df.iloc[1:]

#Streaming transposed data
st.dataframe(df)

#Coding linechart
fig = px.line(df, x=df.index, y=df.columns, title='Inflation by Country')
fig.update_xaxes(title='Time')
fig.update_yaxes(title='Inflation')
st.plotly_chart(fig)

#adding sidebar for filtering or something else...

st.sidebar.header('Filters:')
Country = st.sidebar.multiselect(
    'Select Country:',
    options = df.columns.unique(),
    default = None
)

Year = st.sidebar.multiselect(
    'Select Time:',
    options = df.index.unique(),
    default = None
)