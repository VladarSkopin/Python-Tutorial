import random

number_to_guess = random.randint(0, 100)

print('Guess the generated number: ')

continue_game = True
while continue_game:
    try:
        user_number = int(input())
        if user_number < number_to_guess:
            print('Too small')
        elif user_number > number_to_guess:
            print('Too big')
        else:
            print('You are correct!')
            continue_game = False
    except ValueError:
        print('The input number should be an integer!')
print('The End')
