total_amount = float(input('How much is the total amount: '))
print('''Type of payments:
[1] In cash
[2] Credit Card
[3] Installments''')
option = int(input('Type the number of your option: '))
if option == 1:
    discount = total_amount - (total_amount * 20 / 100)
    print('Total amount with discount is {}'.format(discount))
elif option == 2:
    discount = total_amount - (total_amount * 5 / 100)
    print('Total amount with discount is {}'.format(discount))
elif option == 3:
    num_installments = int(input('How many times: '))
    if num_installments == 2:
        total = total_amount + (total_amount * 20 / 100)
        installments = total / 2
        print('Your bill will be split in 2x.')
        print('Your bill is {} and will cost {}'. format(total_amount, total))
    elif num_installments == 3:
        total = total_amount + (total_amount * 20 / 100)
        installments = total / 3
        print('Your bill will be split in 3x.')
        print('Your bill is {} and will cost {}'.format(total_amount, total))






