import requests

api = 'a5832fa79f6a1c15cfc2e9ca08631df3'

def get_weather(city):

    # Удаление случайных пробелов
    city = city.replace(" ", "")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric&lang=ru"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        weather = data['weather'][0]
        main = data['main']
        wind = data['wind']

        result = (
            f"Город: {city}\n"
            f"Температура: {round(main['temp'])}\n"
            f"Влажность: {main['humidity']}\n"
            f"Описание: {weather['description']}\n"
            f"Скорость ветра: {wind['speed']}\n"
        )

        print(result)
        return result

    else:
        return f"Не удалось получить данные о городе {city}"


if __name__ == "__main__":
    get_weather()