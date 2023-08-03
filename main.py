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


def main():
    locations = ['Лондон', 'Шереметьево', 'Череповец']
    for location in locations:
        print(check_weather(location))


if __name__ == '__main__':
    main()
