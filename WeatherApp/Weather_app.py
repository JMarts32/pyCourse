from io import BytesIO
import requests
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
    new_size = (icon_image.width * 4, icon_image.height * 4)
    resized_icon_image = icon_image.resize(new_size)
    resized_icon_photo = ImageTk.PhotoImage(resized_icon_image)
    weather_icon_label.config(image=resized_icon_photo)
    weather_icon_label.image = resized_icon_photo

    # Update the time label
    time_label.config(text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# Create the main window
root = Tk()
root.title("Weather App")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - 900) // 2
y_coordinate = (screen_height - 500) // 2
root.geometry(f"900x500+{x_coordinate}+{y_coordinate}")
root.configure(bg="#73cfe5")

# Create the location entry
location_label = ttk.Label(root, text="Enter Location:")
location_label.config(font=('Helvetica', 24, "bold"), background="#73cfe5")
location_label.grid(row=0, column=1)
location_entry = ttk.Entry(root)
location_entry.grid(row=0, column=2)
location_entry.focus()

# Create the get weather button
get_weather_button = ttk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.grid(row=0, column=3)

# Create the weather data labels
temperature_label = ttk.Label(root, text="Temperature:")
temperature_label.config(font=('Helvetica', 18), background="#73cfe5")
temperature_label.grid(row=1, column=0, pady=(0, 10))

humidity_label = ttk.Label(root, text="Humidity:")
humidity_label.config(font=('Helvetica', 18), background="#73cfe5")
humidity_label.grid(row=2, column=0, pady=(0, 10))

wind_speed_label = ttk.Label(root, text="Wind Speed:")
wind_speed_label.config(font=('Helvetica', 18), background="#73cfe5")
wind_speed_label.grid(row=3, column=0, pady=(0, 10))

# Create the weather icon label
weather_icon_label = ttk.Label(root)
weather_icon_label.config(background="#73cfe5")
weather_icon_label.place(x=450, y=120)

# Create the time label
time_label = ttk.Label(root, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
time_label.config(font=('Helvetica', 18), background="#73cfe5")
time_label.grid(row=4, column=0, pady=(0, 10))

# Configure row weights to evenly distribute labels vertically
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Run the main loop
root.mainloop()