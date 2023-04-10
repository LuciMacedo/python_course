num = int(input('Type a number: '))
total = 0
for n in range(1, num + 1):
    if num % n == 0:
        total += 1
if total == 2:
    print('It is a prime number')
else:
    print('It is not a prime number')