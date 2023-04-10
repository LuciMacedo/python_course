r1 = int(input('Type measure: '))
r2 = int(input('Type measure: '))
r3 = int(input('Type measure: '))

if r1 < r3 + r2 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Can be a triangle!')
else:
    print("Can't be a triangle!")