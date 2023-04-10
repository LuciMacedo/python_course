from random import randint
pc_guess = randint(0, 10)
gamer_guess = int(input('Type a number: '))
get_it = False
count = 0
while not get_it:
    gamer_guess = int(input('Type a number: '))
    count += 1
    if gamer_guess == pc_guess:
        get_it = True
print('Well done! You made it in {}'.format(count))

