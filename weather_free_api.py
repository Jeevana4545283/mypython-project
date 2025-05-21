import requests

def fetch_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        current = data['current_condition'][0]
        temp_c = current['temp_C']
        weather_desc = current['weatherDesc'][0]['value']
        humidity = current['humidity']
        wind_speed = current['windspeedKmph']

        print(f"\nWeather in {city.capitalize()}:")
        print(f"Description: {weather_desc}")
        print(f"Temperature: {temp_c}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
    except KeyError:
        print("Unexpected data format. Try a different city.")

if __name__ == "__main__":
    city = input("Enter a city name to get current weather: ").strip()
    fetch_weather(city)
