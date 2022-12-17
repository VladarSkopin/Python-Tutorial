import random


class InvalidGameChoiceError(Exception):
    def __init__(self, value):  # constructor for this exception
        self.value = value


def get_choice_string(x):
    if x == 1:
        return 'scissors'
    elif x == 2:
        return 'rock'
    elif x == 3:
        return 'paper'
    else:
        return 'unknown choice'


def game_fight(user_number, computer_number):
    if (user_number == 1 and computer_number == 3) or (user_number == 2 and computer_number == 1) or (user_number == 3 and computer_number == 2):
        return 'victory'
    elif (user_number == 1 and computer_number == 2) or (user_number == 2 and computer_number == 3) or (user_number == 3 and computer_number == 1):
        return 'fail'
    else:
        return 'tie'


computer_choice = random.randint(1, 3)

user_victory_count = 0
computer_victory_count = 0

continue_game = True
while continue_game:
    try:
        print('Make your choice (1 - scissors, 2 - rock, 3 - paper): ')
        user_choice = int(input())
        if user_choice < 1 or user_choice > 3:
            raise InvalidGameChoiceError('Your choice can only be 1, 2, or 3')
        computer_choice = random.randint(1, 3)
        print(f'You chose: {get_choice_string(user_choice)}')
        print(f'Computer chose: {get_choice_string(computer_choice)}')
        game_message = game_fight(user_choice, computer_choice)
        if game_message == 'victory':
            print('You\'ve won this round!')
            user_victory_count += 1
        elif game_message == 'fail':
            print('You fail this round')
            computer_victory_count += 1
        else:
            print('It\'s a tie')
        print(f'Your count so far: {user_victory_count} scores')
        print(f'Computer count so far: {computer_victory_count} scores')
        print('-----')
        if user_victory_count == 3:
            print('You\'ve gained 3 scores! You are the final winner! CONGRATULATIONS :-)')
            continue_game = False
        if computer_victory_count == 3:
            print('Computer have gained 3 scores. You lose the game.')
            continue_game = False
    except TypeError:
        print('Your choice number should be an integer!')
    except InvalidGameChoiceError as igce:
        print(igce)

print('----------')
print('The End')
