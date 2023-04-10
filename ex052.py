phrase = str(input('Type a phrase: ')).strip().upper()
word = phrase.split()
joined = ''.join(word)
reverse_word = ''
for char in range(len(joined)-1, -1, -1):
    reverse_word += joined[char]

if joined == reverse_word:
    print('Its is palindrome')
else:
    print('Its not a palindrome')

print(reverse_word)