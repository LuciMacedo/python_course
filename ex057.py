person_gender = str(input('Type your gender [F/M]:  ')).strip().upper()[0]
while person_gender not in 'FM':
    person_gender = str(input('Invalid information. Type your gender: [F/M]')).strip().upper()[0]
print('Gender {} saved.'.format(person_gender))
