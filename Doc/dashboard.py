import pandas as pd
import plotly.express as px
import streamlit as st

#CONFIG STREAMLIT
st.set_page_config(page_title='Inflation in EU',
                   page_icon = 'bar_chart:',
                   layout = 'wide')

#MAINPAGE
st.title(':bar_chart: EU Inflation Statistic Dashboard')
st.markdown('###')

df = pd.read_excel(
    io = 'data\sorted_data\Inflation_in_EU.xlsx',
    engine ='openpyxl',
    usecols = 'A:DQ',
    nrows = 1000,
)

#Transposing data table
df = df.T
df.columns = df.iloc[0]
df = df.iloc[1:]

#Getting most recent date out of dates_row
dates_row = df.index
dates = pd.to_datetime(dates_row,format='%Y-%m')
most_recent = dates.max()
str_most_recent = most_recent.strftime('%Y-%m')

#TOP-INFLATION
selected_data = df.loc[str_most_recent]
selected_data = pd.to_numeric(selected_data.squeeze(), errors='coerce')
highest_inflation = selected_data.max()
country_with_highest_inflation = selected_data.idxmax()
#LOWEST-INFLATION
selected_data2 = df.loc[str_most_recent]
selected_data2 = pd.to_numeric(selected_data2.squeeze(), errors='coerce')
lowest_inflation = selected_data2.min()
country_with_lowest_inflation = selected_data2.idxmin()
#POLAND-INFLATION
selected_poland = df.loc[str_most_recent,'Poland']
if pd.isna(selected_poland):
    previous_date = most_recent - pd.DateOffset(months=1)
    str_previous_date = previous_date.strftime('%Y-%m')
    selected_poland = df.loc[str_previous_date, 'Poland']


left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader('Top inflation')
    st.subheader(country_with_highest_inflation)
    st.subheader(f'{highest_inflation:,}')

with middle_column:
    st.subheader('In Poland')
    st.subheader(selected_poland)
    
    
with right_column:
    st.subheader('Lowest inflation:')
    st.subheader(country_with_lowest_inflation)
    st.subheader(lowest_inflation)
st.markdown('---')

#SIDEBAR-FILTERS
st.sidebar.header('Filters:')
Country = st.sidebar.multiselect(
    'Select Country:',
    options = df.columns.unique(),
    default = ['Poland', 'Germany', 'France', 'Spain', 'Portugal', 'Italy']
)

Year = st.sidebar.multiselect(
    'Select Time:',
    options = df.index.unique(),
    default = str_most_recent
)

selected_countries = Country
selected_years = Year

#STREAMING SELECTED DATA
st.subheader('Data selected by filters:')
df_selection = df.loc[df.index.isin(selected_years), selected_countries]
st.dataframe(df_selection)

#LINECHART
st.subheader('Linechart')
fig = px.line(df, x=df.index, y=df.columns, title='Inflation by Country')
fig.update_xaxes(title='Time')
fig.update_yaxes(title='Inflation')
fig.update_layout(width=1500, height=800)
st.plotly_chart(fig)

#STREAMING DATA
st.subheader('All of Data')
st.dataframe(df)