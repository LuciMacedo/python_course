km = float(input('How many km did you used: '))
d = int(input('How many days:'))
total_d = d * 60
total_km = km * 0.15
total_amount = total_d + total_km
print('The total amount for {} days and km {} is ${:.2f}.'.format(d, km, total_amount))
