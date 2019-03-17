# Written for Python 3
import random
import os

characters = ["Dora", "Boots", "Isa", "Swiper", "Benny", "Tico"]
colors = ["Green", "Red", "Yellow", "Blue", "Orange"]
print('Let\'s Play!!! (Press Enter to Begin or q and Enter to quit)')
while True:
    character = random.choice(characters)
    color = random.choice(colors)
    s = input()
    if s == ('q'):
        print('Thanks for playing!')
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(character + '\n' + color)
