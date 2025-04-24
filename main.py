import streamlit as st
import plotly_express as px


st.title("Weather Forecast for the Week")

place = st.text_input("Place:")

days = st.slider("Forecast Days:", min_value=1, max_value=5, help="Select number of days")

option = st.selectbox("Select data to view:",
                      ("Temperature","Sky"))

st.header(f"{option} for the next {days} days in {place}")

def get_data(day):
    date = ["2024-02-02","2024-03-03", "2024-04-04"]
    temp = [15, 23, 44]
    temp = [day * i for i in temp]
    return date, temp

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x":"Date", "y": "Temperature"})
st.plotly_chart(figure)