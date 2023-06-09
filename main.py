import streamlit as st
import plotly.express as px

continent = st.selectbox(label='Benua', options=['Asia', 'Africa', 'Americas', 'Europe', 'Oceania'])

# Load Asia's GDP
df = px.data.gapminder().query(f"continent=='{continent}'")

st.title(f'{continent} GDP from 1952-2007')
st.table(df)