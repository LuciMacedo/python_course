def score_player(name='<an-know>', goals=0):
    print(f'The player is {name} he scored {goals} gols.')


n = str(input('Player name: '))
g = str(input('How many gols the player scored: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    score_player(goals=g)
else:
    score_player(n, g)




