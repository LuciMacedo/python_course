from math import hypot
cat_op = float(input('Type cateto: '))
cat_adj = float(input('Type adj: '))
hi = hypot(cat_op, cat_adj)

print('The hypotenuse is: {:.2f}'.format(hi))

