from random import randint
from time import sleep
from operator import itemgetter

gamers = {
    'gamer1': randint(1, 6),
    'gamer2': randint(1, 6),
    'gamer3': randint(1, 6),
    'gamer4': randint(1, 6)
}
ranking = {}
print(f'Values draw for every gamer {gamers}')

for k, v in gamers.items():
    print(f'{k} draw {v}')
    sleep(1)

ranking = sorted(gamers.items(), key=itemgetter(1), reverse=True)
print('*-' * 30)
print('Ranking dos jogadores')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar {v[1]}.')

