sum_num = 0
count = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        count += 1
        sum_num += n
print(sum_num, count)
