
student_data = {}
student_data['name'] = str(input('Student name is: '))
student_data['score'] = int(input('Student score: '))
print('*-' * 30)
print(f'- name is {student_data["name"]}.')
print(f'- The average is {student_data["score"]}')
if student_data['score'] <= 30:
    student_data["student_status"] = 'failure'
elif 30 < student_data['score'] < 70:
    student_data["student_status"] = 'recuperation'
else:
    student_data["status"] = 'passed'
for k, v in student_data.items():
    print(f'The {k} of the student is {v}')

