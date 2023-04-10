from datetime import date
year = int(input('Type your DOB:'))
current_year = date.today().year
age = 2023 - current_year
military_time = current_year + 18
remain_time = military_time - 2023
print('You was born in {} and are {} years old.'.format(year, age))
if age < 18:
    print('Your military time is going to be {}'.format(remain_time))
elif age > 18:
    print('Your military time was {}'.format(military_time))
else:
    print('You must do it now!')