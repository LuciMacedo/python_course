from shutil import copyfile
'''Simple calculater that outputs the result and also give the user 
the option to see all the outcomes in a new text file.'''


def calculate(first_number, second_number, operation):
    """
    :param first_number: first number entered
    :param second_number: second number entered
    :param operation: operation to be performed
    :return: the result of the equation
    """
    try:
        if operation == 1:
            res = first_number + second_number
            return f'{first_number} + {second_number} = {res:.1f}'
        elif operation == 2:
            res = first_number - second_number
            return f'{first_number} - {second_number} = {res:.1f}'
        elif operation == 3:
            res = first_number * second_number
            return f'{first_number} * {second_number} = {res:.1f}'
        elif operation == 4:
            res = first_number / second_number
            if second_number == 0:
                raise ZeroDivisionError('Division by zero')
            return f'{first_number} / {second_number} = {res:.1f}'
        else:
            raise ValueError('Invalid operation')
    except ZeroDivisionError as e:
        print(f'Erro: {e}')
    except ValueError as e:
        print(f'Erro: {e}')


def write_equation_file(equation):
    """
    :param equation: string datatype - result of the equation
    :return: appending the result in the file.
    """
    with open('equation.txt', 'a') as file:
        file.write("\n" + equation)


def create_new_file(file):
    """
    :param file: file name that the user inputs
    :return: copy of the equation file
    """
    copyfile('equation.txt', f'{file}.txt')
    with open(f'{file}.txt', 'r') as f:
        new_file = f.read()
        print(new_file)


# Infinity loop for the user inputs and validations.
while True:
    try:
        first_number = int(input('Enter the first number: '))
        print('=-' * 38)
        second_number = int(input('Enter the second number: '))
        print('=-' * 38)
        print('''Which operation do want to perform?
          [1] Sum
          [2] Minus
          [3] Multiplication
          [4] Division
          ''')
        operation = int(input('Enter one option: '))
        print('=-' * 38)

        # variable to store the return of the calculate function.
        result = (calculate(first_number, second_number, operation))
        # check if the result is not None and write the result in the equation file.
        if result is not None:
            print(result)
            write_equation_file(result)

        # option for new inputs or finish the program
        print('=-' * 38)
        print('''What do you want to do now?
          [1] Enter new numbers.
          [2] Finish and read all equations. ''')
        user_answer = int(input('Enter your option: '))

        # getting the file name and calling the functing to create new file.
        if user_answer == 2:
            file_name = str(input('Create a file for your equation: '))
            create_new_file(file_name)
            break
        # check if the option is not invalid.
        elif user_answer != 1:
            print('Ooops... That was not valid! Try again.')
            break
    except ValueError:
        print(f'Ooops... That was not valid! Try again. ')
print('THE END!!!')
