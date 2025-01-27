import requests

def get_weather(city):
    api_key = "015c5dc93de1e72ea81c48eb25f41108"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }
        return weather
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    city = input("Enter the city name: ")
    weather_data = get_weather(city)
    if weather_data:
        print(f"City: {weather_data['city']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Weather: {weather_data['description'].capitalize()}")
    else:
        print("Unable to fetch weather data. Please try again.")
