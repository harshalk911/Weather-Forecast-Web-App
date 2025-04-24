import streamlit as st
from click import style

st.title("Weather Forecast for the Week")

place = st.text_input("Place:")

days = st.slider("Forecast Days:", min_value=1, max_value=5, help="Select number of days")

option = st.selectbox("Select data to view:",
                      ("Temperature","Sky"))

st.header(f"{option} for the next {days} days in {place}")

