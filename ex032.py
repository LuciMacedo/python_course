from datetime import date
year = int(input('Enter the year or 0 for the current year: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('The {} is bi'.format(year))
else:
    print('The {} is not bi'.format(year))
