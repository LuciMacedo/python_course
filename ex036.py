house_price = float(input('How much is the house?'))
salary = float(input('How much do you earn?'))
duration = int(input('How years to pay off your house?'))
value_per_month = salary / duration
limit = (salary * 30) / 100
if value_per_month > limit:
    print('I am sorry but you cannot take the loan')
else:
    print('You can take the loan.')
    