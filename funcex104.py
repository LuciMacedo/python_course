def readintt(msg):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            ok = True
            value = int(n)
        else:
            print('Type a valid number!')
        if ok:
            break
    return value


user_input = readintt('Type a number: ')
print(f'You typed number {user_input}')





