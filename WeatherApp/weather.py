import tkinter as tk
import requests
import time


API_KEY = "06c921750b9a82d8f5d1294e1586276f"


def create_weather_api_url(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    url = f"{base_url}?q={city}&appid={API_KEY}"
    return url


def get_weather(canvas):
    city = textField.get()
    api_url = create_weather_api_url(city)
    
    json_data = requests.get(api_url).json()
    weather = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = f"{city.upper()}\n{weather}\n{temp}°C" 
    final_data = (
        f"\nMin Temp: {min_temp}°C\n"
        f"Max Temp: {max_temp}°C\n"
        f"Pressure: {pressure}\n"
        f"Humidity: {humidity}\n"
        f"Wind Speed: {wind}\n"
        f"Sunrise: {sunrise}\n"
        f"Sunset: {sunset}"
    )
    
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("800x700")
canvas.title("Python Weather App")
font_large = ("poppins", 50, "bold")
font_small = ("poppins", 15, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=font_large)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', get_weather)

label1 = tk.Label(canvas, font=font_large)
label1.pack()
label2 = tk.Label(canvas, font=font_small)
label2.pack()

canvas.mainloop()
