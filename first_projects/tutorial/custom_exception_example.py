# custom exception type
class InvalidAgeError(Exception):
    def __init__(self, value):  # constructor for this exception
        self.value = value


try:
    age = int(input('How old are you?: '))
    if age <= 0 or age >= 140:
        raise InvalidAgeError('Sorry, that age doesn\'t seem valid')
    print(f'{age} is a perfect age to study programming!')
except ValueError:
    print('Invalid integer was entered')
except InvalidAgeError as iae:
    print(iae)
finally:
    print('Thank you for using our service')

