most = 0
less = 0

for c in range(1, 5):
    weight = float(input('Weight for the {} person: '.format(c)))
    if c == 1:
        most = weight
        less = weight
    else:
        if weight < less:
            less = weight
        if weight > most:
            most = weight
print('The most high weight is {} e the most lower is {}'.format(most, less))
