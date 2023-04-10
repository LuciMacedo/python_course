age_sum = 0
age_average = 0
man_age = 0
man_name = ''
woman_age = 0
for person in range(1, 4):
    person_name = str(input('Type your name: '))
    person_age = int(input('Type your age: '))
    person_gender = str(input('Type your gender [F]Female and [M]Male: ')).strip()
    age_sum += person_age
    if person == 1 and person_gender in 'Mn':
        man_age = person_age
        man_name = person_name
    if person_gender in 'Mn' and person_age > man_age:
        man_age = person_age
        man_name = person_name
    if person_gender in 'Ff' and person_age < 20:
        woman_age += 1
age_average = age_sum / 3
print('The average are is {}'.format(age_average))
print('The oldest man is {} with {}'.format(man_name, man_age))
print('There are {} women under 20.'.format(woman_age))
