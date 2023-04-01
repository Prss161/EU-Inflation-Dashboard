import pandas as pd
import plotly.express as px
import streamlit as st

#Need to think about scraping data from website eu statista with panda.
#CONFIG STREAMLIT
st.set_page_config(page_title='Inflation in EU',
                   page_icon = 'bar_chart:',
                   layout = 'wide')

#MAINPAGE
st.title(':bar_chart: EU Inflation Statistic Dashboard')
st.markdown('##')

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

#TOP-INFLATION
selected_data = df.loc[['2023-01']]
selected_data = pd.to_numeric(selected_data.squeeze(), errors='coerce')
highest_inflation = selected_data.max()
country_with_highest_inflation = selected_data.idxmax()
#LOWEST-INFLATION
selected_data2 = df.loc['2023-01']
selected_data2 = pd.to_numeric(selected_data2.squeeze(), errors='coerce')
lowest_inflation = selected_data2.min()
country_with_lowest_inflation = selected_data2.idxmin()
#POLAND-INFLATION


left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader('Top inflation')
    st.subheader(country_with_highest_inflation)
    st.subheader(f'{highest_inflation:,}')

with middle_column:
    st.subheader('In Poland')
    
    
with right_column:
    st.subheader('Lowest inflation:')
    st.subheader(country_with_lowest_inflation)
    st.subheader(lowest_inflation)

#Streaming transposed data
st.dataframe(df)

#SIDEBAR-FILTERS

st.sidebar.header('Filters:')
Country = st.sidebar.multiselect(
    'Select Country:',
    options = df.columns.unique(),
    default = 'Poland'
)

Year = st.sidebar.multiselect(
    'Select Time:',
    options = df.index.unique(),
    default = '2023-02'
)

selected_countries = Country
selected_years = Year

#STREAMING SELECTED DATA
df_selection = df.loc[df.index.isin(selected_years), selected_countries]
st.dataframe(df_selection)

#LINECHART
fig = px.line(df, x=df.index, y=df.columns, title='Inflation by Country')
fig.update_xaxes(title='Time')
fig.update_yaxes(title='Inflation')
st.plotly_chart(fig)