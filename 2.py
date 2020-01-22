f = open('Задача2.txt', 'r')
l = [line for line in f]
for i in range(3):
	l[i] = int(l[i])
l[3] = l[3].split()
for i in range(len(l[3])):
	l[3][i] = int(l[3][i])
f.close()

size = l[0]
M = l[2]
N = l[1]

def Next(a: list, n: int, m: int):
	j = m - 1
	while a[j] == n and j >= 0:
		j -= 1
	if j < 0: return False
	if a[j] >= n: j -= 1
	a[j] += 1
	if j == m - 1: return True
	k = j + 1
	while k < m:
		a[k] = 1
		k += 1
	return True

def solve(lst: list, l: list, size: int):
	summ = 0
	for i in range(len(lst)):
		summ += l[3][lst[i] - 1]
	return True if summ == size else False
	
def answer(lst: list, l: list):
	counts = []
	for i in range(len(l[3])):
		counter = 0
		for j in lst:
			counter += 1 if i == j - 1 else 0
		counts.append(counter)
	for i in range(len(counts)):
		print('{0} шт. по {1} м;'.format(counts[i],lst[i]), end = ' ')
	print()
	
h = N if N > M else M
lst = [1 for i in range(h)]
while True:
	if Next(lst, N, M):
		if solve(lst, l, size):
			answer(lst, l)
	else:
		break