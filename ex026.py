phrase = str(input('Type a phrase')).upper()
letter_a = phrase.count('A')
print('There is {} letters A on the phrase'.format(letter_a))
letter_fposition = phrase.find('A')
print('The first letter A is on {} position'.format(letter_fposition))
letter_lposition = phrase.rfind('A')
print('The last position is {}'.format(letter_lposition))

