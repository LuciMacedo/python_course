salary = float(input('Type your salary: '))
if salary <= 1250.00:
    new_salary = (salary * 15) / 100 + salary
else:
    new_salary = (salary * 10) / 100 + salary
print('You new salary is £{:.2f}'.format(new_salary))