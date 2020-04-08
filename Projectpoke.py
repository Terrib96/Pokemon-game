import random

from PIL import Image
import requests


import sys

import vlc

import time

sound_file = vlc.MediaPlayer("file:///Users/terribroughton/Desktop/pokemonmusic.mp3")
sound_file.play()
time.sleep(5)




# Delay printing
def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)



delay_print("Welcome to the Pokemon Top Trumps Game!!     ")



new_player_name = input('What is the name of the new player?: ')

delay_print("Hello " + new_player_name + ", get ready for the Pokemon Battle!\n")
computername = " The Computer"
delay_print("You are playing against" + computername + ", get ready...\n")


with open('ranking.txt', 'r') as text_file:
   ranking = text_file.read()
   ranking = ranking + new_player_name + '\n'


with open('ranking.txt', 'w+') as text_file:
   text_file.write(ranking)






def random_pokemon():
    pokemon_number = random.randint(1,151)
    delay_print("random number between 1 and 151 is % d" % (pokemon_number))
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return pokemon


def run():
    my_pokemon = random_pokemon()

    delay_print(' , You were given {}'.format(my_pokemon['name'] ) )
    stat_choice = input(' , Which stat do you want to use? (id, height, weight, base_experience, order,) '  )

    opponent_pokemon = random_pokemon()
    delay_print(' , The opponent chose {}'.format(opponent_pokemon['name'] ) )

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]


    if my_stat > opponent_stat:
        delay_print('...........You Win!')
        winner_img = Image.open('winner.jpg')
        winner_img.show()

    elif my_stat < opponent_stat:
        delay_print('.........You Lose!')
        loser2_img = Image.open('loser2.jpg')
        loser2_img.show()

    else :
        delay_print('.........Draw!')
        draw_img = Image.open('draw.jpg')
        draw_img.show()





run()




