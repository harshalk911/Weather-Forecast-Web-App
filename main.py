import streamlit as st
import plotly_express as px
from backend import get_data


st.title("Weather Forecast for the Week")

place = st.text_input("Place:")

days = st.slider("Forecast Days:", min_value=1, max_value=5, help="Select number of days")

option = st.selectbox("Select data to view:",
                      ("Temperature","Sky"))

st.header(f"{option} for the next {days} days in {place}")

data  = get_data(place, days, option)




figure = px.line(x=d, y=t, labels={"x":"Date", "y": "Temperature"})
st.plotly_chart(figure)