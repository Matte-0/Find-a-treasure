print('Welcome to the treasure island.'
      '\nYour mission is to find the treasure. Good Luck!')
choice1 = input('Choose where do you want to go:'
                'Type "Left" or "Right": ').lower()
if choice1 == ('left'):
    choice2 = input('You have come to a lake.'
                    '\nThere is an island in the middle of the lake.'
          '\nType "wait" if you want to wait a boat or "swim" '
                    'if you want just swim to the island: ').lower()
    if choice2 == 'swim':
        choice3 = input('You have come to the island. There is a house with 3 doors: '
                        'Yellow, Red and Blue doors.'
                        '\nwhich one do you want to choose: ').lower()
        if choice3 == 'yellow':
            print('Congratulations! You found the treasure!')
        elif choice3 == 'red':
            print("It's a room full of fire! Game Over.")
        elif choice3 == 'blue':
            print('You enter a room of beasts! Game Over.')

        else:
            print('Sorry, I don\'t understand that.')

    else:
        print('There were Wolves, and they killed you. Game over.')
else:
    print('You fell in to a hole. Game Over.')



