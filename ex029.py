speed = float(input('Enter your speed: '))
ticket_cost = (speed - 80) * 7
if speed > 80:
    print('You got a ticket! You have to pay £{}'.format(ticket_cost))
print('Have good morning!')