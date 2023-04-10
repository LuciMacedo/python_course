number_lst = []
for c in range(0, 5):
    n = int(input('Type a number: '))
    if c == 0 or n >= number_lst[-1]:
        number_lst.append(n)
    else:
        pos = 0
        while pos < len(number_lst):
            if n <= number_lst[pos]:
                number_lst.insert(pos, n)
                break
            pos += 1
print(f'The typed numbers are {number_lst}')



