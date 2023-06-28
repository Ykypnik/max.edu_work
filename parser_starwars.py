import requests


def biggest_planet():
    responce = requests.get('https://swapi.dev/api/planets/')
    responce = responce.json()

    all_planets = responce["results"]

    diameter_and_name = {}
    diameter = []

    for i in range(len(all_planets)):
        diameter_new = all_planets[i]['diameter']
        diameter.append(int(diameter_new))
        diameter_and_name[diameter_new] = all_planets[i]['name']

    max_diameter = max(diameter)
    name_the_biggest_planets = f'Самая большая планета {diameter_and_name[str(max_diameter)]} из Звёздные Войны имеет диаметр {max_diameter}'
    return str(name_the_biggest_planets)

def fastest_starship():
    responce = requests.get('https://swapi.dev/api/starships/')
    responce = responce.json()

    all_starship = responce['results']

    speed_and_name_ss = {}
    speed_ss = []

    for i in range(len(all_starship)):
        try:
            speed = int(all_starship[i]['max_atmosphering_speed'])
            speed_ss.append(speed)
            speed_and_name_ss[speed] = all_starship[i]['name']
        except:
            speed = all_starship[i]['max_atmosphering_speed']

    max_speed = max(speed_ss)
    thefastssname = speed_and_name_ss[max_speed]
    print(f'Самый быстрый космичекий корабль {thefastssname} имеет скорость {max_speed}')
    return str(f'Самый быстрый космичекий корабль {thefastssname} имеет скорость {max_speed}')