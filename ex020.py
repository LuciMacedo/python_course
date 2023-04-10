from random import shuffle

std0 = str(input('Students name: '))
std1 = str(input('Students name: '))
std2 = str(input('Students name: '))
std3 = str(input('Students name: '))
std4 = str(input('Students name: '))

student_list = [std0, std1, std2, std3, std4]
shuffle(student_list)
print(student_list)