#Madlibs Game
'''
One day, I found a (1. adjective) (2. animal) outside my house. It was (3. verb-ing) while singing songs by Taylor Swift. Suddenly, it threw a giant (5. food) into the air and ran toward (6. place) screaming, “(10. silly word)!”
I felt extremely (7. emotion), so I grabbed my lucky (8. random object) and chased after it for (9. number) minutes. In the end, the strange creature disappeared into a cloud of glitter, leaving behind only the smell of burnt pizza and mystery.
'''
#Introduction
print('Hello User! What is your name?')
name = input('Enter your name: ')
print('WELCOME TO MADLIBS GAME!')
print('Now its time to create your story')
print('Enter the following:')

#User Input:
title = input('Create a TITLE for your story: ').upper()
adjective = input('Adjective: ').lower()
animal = input('Animal: ').lower()
verb = input('Verb-ing:').lower()
music_artist = input('Music Artist: ')
food = input('food: ').lower()
place = input('Place: ')
silly_word = input('Silly Word/Sudden Reaction: ').upper()
emotion = input('Emotion: ').lower()
random_object = input('Random Object: ').lower()
number = int(input('Number: '))

#modification:

#Story Output:
print({title})
print(f'Written by {name}')
print(f'One day, I found a {adjective} {animal} outside my house.')
print(f'It was {verb} while singing songs by {music_artist}.')
print(f'Suddenly, it threw a giant {food} into the air and ran toward {place} screaming, {silly_word}!')
print()
print(f'I felt extremely {emotion}, so I grabbed my lucky {random_object} and chased after it for {number} minutes.')
print('In the end, the strange creature disappeared into a cloud of glitter, leaving behind only the smell of burnt pizza and mystery.')


