from datetime import date
employee_data = {}
employee_data['name'] = str(input('Employee name: '))
employee_dob = int(input('Employee DOB: '))
employee_data['employee_age'] = date.today().year - employee_dob
employee_data['work_permit'] = int(input('CT number(if not type 0): '))
if employee_data['work_permit'] != 0:
    employee_data['contract_date'] = int(input('Start year: '))
    employee_data['salary'] = float(input('The employee salary: '))
    employee_data['retired'] = (employee_data['contract_date'] + 35) - employee_dob
print('*-' * 30)

for k, v in employee_data.items():
    print(f'{k} has the value {v}')





