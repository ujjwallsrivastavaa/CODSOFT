import tkinter as tk
import requests

def get_weather():
    api_key = "097327848fb34bfe7659f660758d7596"
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    weather_description = data["weather"][0]["description"]

    weather_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nDescription: {weather_description}")

root = tk.Tk()
root.title("Weather Forecast")

city_label = tk.Label(root, text="Enter City Name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

weather_label = tk.Label(root, text="", font=("Helvetica", 12))
weather_label.pack()

root.mainloop()
