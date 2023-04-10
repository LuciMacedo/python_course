from datetime import date

current_year = date.today().year
over = 0
under = 0

for c in range(1, 4):
    dob = int(input('When did you was born person {}: '.format(c)))
    age = current_year - dob
    if age >= 21:
        over += 1
    elif age < 21:
        under += 1

print('{} are under 21 and {} are over 21'.format(under, over))

