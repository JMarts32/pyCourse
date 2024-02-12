import tkinter as tk
from tkinter import ttk
import pandas as pd
import requests
import WeatherApp_Controller as controller
from geopy.geocoders import Nominatim

temp = 0
wind_speed = 0

def update_weather(location):
    geolocator = Nominatim(user_agent="Geopy Library")
    value = geolocator.geocode(location)
    print(value.address)
    # wind_speed = controller.update_weather(location)[1]
    # temp = controller.update_weather(location)[0]

# Main window
root = tk.Tk()
root.title("Weather App")
root.geometry("900x500")

# this centers the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - 900) // 2
y_coordinate = (screen_height - 500) // 2
root.geometry(f"900x500+{x_coordinate}+{y_coordinate}")

# Color of the background
canvas = tk.Canvas(root, width=900, height=500, highlightthickness=0)
canvas.grid(row=0, column=0, rowspan=4, columnspan=4)
for i in range(500):
    shade = "#{:02x}{:02x}{:02x}".format(51 + i // 3, 102 + i // 6, 204 + i // 12)
    canvas.create_line(0, i, 900, i, fill=shade, width=1)

# Location labels and entry
location_label = tk.Label(root, text="Enter Location:", font=('Helvetica', 24, "bold"))
location_label.grid(row=0, column=2, padx=10, pady=10, sticky="e")
location_entry = tk.Entry(root,font=('Helvetica', 24))
location_entry.grid(row=0, column=3, padx=10, pady=10, sticky="w")
location_entry.focus()

# Actual temperature
current_temperature_label = ttk.Label(root, text="Temperature: ", font=('Helvetica', 18))
current_temperature_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Actual wind speed
current_wind_speed_label = ttk.Label(root, text="Wind Speed: ", font=('Helvetica', 18))
current_wind_speed_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Image for the weather
weather_image_label = ttk.Label(root, text="Weather Image", font=('Helvetica', 16, 'bold'))
weather_image_label.place(x=500,y=300)

# Update the weather button
update_button = ttk.Button(root, text="Update Weather", command=update_weather("Bogota"))
update_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# This makes the window expandable
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

# Style
style = ttk.Style()
style.configure('TButton', background='#ffffff')

# Start the loop
root.mainloop()
