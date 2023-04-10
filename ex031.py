distance = int(input('How long is your travel: '))
if distance < 200:
    cost1 = distance * 0.50
    print('Your travel will cost {}'.format(cost1))
else:
    cost2 = distance * 0.45
    print('Your travel will cost {}'.format(cost2))
print('Have a save trip!')
