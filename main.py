import streamlit as st
import plotly.express as px

# Load Asia's GDP
df = px.data.gapminder().query("continent=='Asia'")

st.title('Asia GDP from 1952-2007')
st.table(df)
