import tkinter as tk
from tkinter import ttk
import WeatherApp_Controller as controller

temp = 0
wind_speed = 0

def update_weather(location):
    return controller.update_weather(location)

# Crear la ventana principal
root = tk.Tk()
root.title("Weather App")
root.geometry("900x500")

# Centrar la ventana en la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - 900) // 2
y_coordinate = (screen_height - 500) // 2
root.geometry(f"900x500+{x_coordinate}+{y_coordinate}")

# Canvas para el fondo degradado
canvas = tk.Canvas(root, width=900, height=500, highlightthickness=0)
canvas.grid(row=0, column=0, rowspan=4, columnspan=4)

# Simular degradado azul a blanco con líneas
for i in range(500):
    shade = "#{:02x}{:02x}{:02x}".format(51 + i // 3, 102 + i // 6, 204 + i // 12)
    canvas.create_line(0, i, 900, i, fill=shade, width=1)

# Etiqueta y cuadro de entrada para la ubicación
location_label = tk.Label(root, text="Enter Location:", font=('Helvetica', 24, "bold"))
location_label.grid(row=0, column=2, padx=10, pady=10, sticky="e")
location_entry = tk.Entry(root,font=('Helvetica', 24))
location_entry.grid(row=0, column=3, padx=10, pady=10, sticky="w")
location_entry.focus()

# Etiqueta para mostrar la temperatura actual
current_temperature_label = ttk.Label(root, text="Temperature: ", font=('Helvetica', 18))
current_temperature_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Etiqueta para mostrar la velocidad del viento actual
current_wind_speed_label = ttk.Label(root, text="Wind Speed: ", font=('Helvetica', 18))
current_wind_speed_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Espacio para la imagen del clima
weather_image_label = ttk.Label(root, text="Weather Image", font=('Helvetica', 16, 'bold'))
weather_image_label.place(x=500,y=300)

# Botón para actualizar la información del clima
update_button = ttk.Button(root, text="Update Weather", command=update_weather)
update_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Configurar pesos de las filas y columnas para que la imagen se expanda
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

# Estilo para el botón
style = ttk.Style()
style.configure('TButton', background='#ffffff')

# Iniciar el bucle principal
root.mainloop()
