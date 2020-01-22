#-*-coding: utf-8-*-
summ = 0
count = 0
for i in range(1000,10000):
	n = i
    while i > 0:
        summ += i % 10
        i //= 10
    if summ * 77 == n:
        print(i)
        count += 1
if count == 0:
    print("Числа не найдены!")