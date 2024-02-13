'''create a weather app that shows the current weather conditions and forecast for a specific location.

Here are the steps you can take to create this project:

    Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.

    Use the json library to parse the JSON data returned by the API call.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

    Use the Pillow library to display the weather icons.

    Use the datetime library to display the current time and date. '''
from io import BytesIO
import requests
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime

# Create a function to get the weather data
def get_weather():
    # Get the API key
    api_key = "194320bc372cf6562146f814a5eab73e"
    # Get the location
    location = location_entry.get()
    # Get the weather data
    url = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
    response = requests.get(url)
    weather_data = response.json()
    # Update the labels with the weather data
    temperature_label.config(text=f"Temperature: {round(int(weather_data['main']['temp'])-273.15,2)}°C")
    humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
    wind_speed_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} m/s")
    # Get the weather icon
    icon_url = f"http://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}.png"
    icon_response = requests.get(icon_url)
    icon_data = icon_response.content
    icon_image = Image.open(BytesIO(icon_data))
    icon_photo = ImageTk.PhotoImage(icon_image)
    weather_icon_label.config(image=icon_photo)
    weather_icon_label.image = icon_photo
    # Update the time label
    time_label.config(text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# Create the main window
root = Tk()
root.title("Weather App")
# Create the location entry
location_label = ttk.Label(root, text="Enter Location:")
location_label.grid(row=0, column=0)
location_entry = ttk.Entry(root)
location_entry.grid(row=0, column=1)
location_entry.focus()
# Create the get weather button
get_weather_button = ttk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.grid(row=0, column=2)
# Create the weather data labels
temperature_label = ttk.Label(root, text="Temperature:")
temperature_label.grid(row=1, column=0)
humidity_label = ttk.Label(root, text="Humidity:")
humidity_label.grid(row=2, column=0)
wind_speed_label = ttk.Label(root, text="Wind Speed:")
wind_speed_label.grid(row=3, column=0)
# Create the weather icon label
weather_icon_label = ttk.Label(root)
weather_icon_label.grid(row=1, column=1, rowspan=3)
# Create the time label
time_label = ttk.Label(root, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
time_label.grid(row=4, column=0)
# Run the main loop
root.mainloop()