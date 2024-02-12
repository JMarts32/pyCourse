# WeatherApp_Controller.py
import WeatherApp_Model

def update_weather(location_entry):
    location = location_entry.get()
    latitude = 40.7128  # Latitud de Nueva York (Ejemplo)
    longitude = -74.0060  # Longitud de Nueva York (Ejemplo)
    current_temperature, current_wind_speed, hourly_data = WeatherApp_Model.update_weather(latitude, longitude)
    return current_temperature, current_wind_speed
