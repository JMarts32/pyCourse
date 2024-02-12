import requests

def update_weather(latitude, longitude):
    current_temperature = 0
    current_wind_speed = 0
    hourly_data = {"time": [], "temperature": [], "relative_humidity": [], "wind_speed": []}

    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    try:
        response = requests.get(api_url)
        data = response.json()

        # Actualizar datos del tiempo actual
        current_data = data.get("current", {})
        current_temperature = current_data.get("temperature_2m", 0)
        current_wind_speed = current_data.get("wind_speed_10m", 0)

        # Actualizar datos por hora
        hourly_data = data.get("hourly", {})
        hourly_data["time"] = hourly_data.get("time", [])
        hourly_data["temperature"] = hourly_data.get("temperature_2m", [])
        hourly_data["relative_humidity"] = hourly_data.get("relative_humidity_2m", [])
        hourly_data["wind_speed"] = hourly_data.get("wind_speed_10m", [])

    except Exception as e:
        print(f"Error updating weather data: {e}")

    return current_temperature, current_wind_speed, hourly_data
