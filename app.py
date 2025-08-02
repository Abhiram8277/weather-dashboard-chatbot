# app.py

import streamlit as st
from weather import get_weather
from chatbot import respond_to_query

st.set_page_config(page_title="Weather Dashboard with Chatbot", layout="centered")

st.title("🌦️ Weather Dashboard + 🤖 Chatbot")
st.markdown("Get real-time weather info and chat using natural language!")

st.header("📍 Weather by City")
city = st.text_input("Enter city name:")
if city:
    data = get_weather(city)
    if data:
        st.success(f"Weather in {data['city']}")
        st.write(f"**Temperature:** {data['temperature']}°C")
        st.write(f"**Condition:** {data['description']}")
        st.write(f"**Humidity:** {data['humidity']}%")
        st.write(f"**Wind Speed:** {data['wind_speed']} m/s")
    else:
        st.error("City not found or API error.")

st.divider()

st.header("💬 Ask the Weather Bot")
query = st.text_input("Your question:")
if query:
    response = respond_to_query(query)
    st.write("🤖:", response)
