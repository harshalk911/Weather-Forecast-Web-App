import streamlit as st
import plotly_express as px

from backend import get_data, get_country

col1 , col2 = st.columns(2)
with col1:
    st.image("weather.png", width=400)

with col2:
    st.title("Minimal Forecast, Maximum Clarity")

place = st.text_input("Location: ", placeholder="Enter the name of City or Town")

days = st.slider("Forecast Days:", min_value=1, max_value=5, help="Select number of days")

option = st.selectbox("Select data to view:",
                      ("Temperature","Sky"))


if place:
    try:
        country_name = get_country(place)
        st.header(f"{option} for the next {days} days in {place.title()}, {country_name}")
        filtered_data = get_data(place, days)

        if option ==  "Temperature":
            temp = [dict["main"]["temp"] / 10 for dict in filtered_data]
            date = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=date, y=temp, labels={"x":"Date", "y": "Temperature(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            date = [dict["dt_txt"] for dict in filtered_data]
            image_label = [s + "\n" + d for s, d in zip(sky_condition, date)]
            images = {"Clouds": "images/cloud.png", "Clear": "images/clear.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_path = [images[condition] for condition in sky_condition]
            st.image(image_path, width=115, caption=image_label)
    except KeyError:
        st.warning("This location does not exist, please enter a valid city name")
