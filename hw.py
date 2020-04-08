import random


import requests


def random_pokemon():
    pokemon_number = random.randint(1,151)
    print("random number between 1 and 151 is % d" % (pokemon_number))
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return pokemon


def run():
    my_pokemon = random_pokemon()

    print('You were given {}'.format(my_pokemon['name'] ) )
    stat_choice = input('Which stat do you want to use? (id, height, weight,) '  )

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name'] ) )

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]


    if my_stat > opponent_stat:
        print('You Win!')

    elif my_stat < opponent_stat:
        print('You Lose!')

    else : print('Draw!')





run()



