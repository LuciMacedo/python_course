words = ('Learn', 'program', 'language', 'python')
for word in words:
    print(f'\n The word {word} has these vowels : ')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter, end='')


