def vote(year):
    from datetime import date
    age = date.today().year - year
    if age >= 18:
        return f'Your age is {age}. Your vote is mandatory. '
    elif 16 <= age < 18 or age >= 65:
        return f'Your age is {age}. Your vote is optional. '
    elif age < 16:
        return f'Your age is {age}. Your do not vote yet. '


user_input = int(input('Type your year of birth: '))

print(vote(user_input))
