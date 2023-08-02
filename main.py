import requests


def check_weather(city):
    payload = {
        'T': '',
        'n': '',
        'M': '',
        'q': '',
        'lang': 'ru'
    }

    url = 'https://wttr.in/'
    request = requests.get(f'{url}/{city}', params=payload)
    request.raise_for_status()
    return request.text


locations = ['Лондон', 'Шереметьево', 'Череповец']
weather = check_weather

for location in locations:
    print(weather(location))
