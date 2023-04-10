first_number = int(input('Type the first number: '))
second_number = int(input('Type the second number: '))
option_operation = 0
while option_operation != 5:
    print(''' 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    option_operation = int(input('What operation do want to do it? '))
    if option_operation == 1:
        res = first_number + second_number
        print('The sum between {} and {} is {}.'.format(first_number, second_number, res))
    elif option_operation == 2:
        mult = first_number * second_number
        print('The multiplication between {} and {} is {}.'.format(first_number, second_number, mult))
    elif option_operation == 3:
        if first_number > second_number:
            greater_number = first_number
        else:
            greater_number = second_number
        print('The greater number is {}.'.format(greater_number))
    elif option_operation == 4:
        first_number = int(input('Type the first number: '))
        second_number = int(input('Type the second number: '))
    elif option_operation == 5:
        print('End!')
    else:
        print('Invalid option!')
print('End!Came back soon!')

