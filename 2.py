f = open('Задача2.txt', 'r')
l = []
for line in f:
	l.append(line)
for i in range(3):
	l[i] = int(l[i])
l[3] = l[3].split()
for i in range(len(l[3])):
	l[3][i] = int(l[3][i])
print(*l,sep='\n')
f.close()

size = l[0]
M = l[1]
N = l[2]

def Next(a: list, n: int, m: int):
	j = m - 1
	while a[j] == n and j >= 0:
		j -= 1
	if j < 0:
		return False
	if a[j] >= n:
		j -= 1
	a[j] += 1
	if j == m - 1:
		return True
	k = j + 1
	while k < m:
		a[k] = a[j]
		k += 1
	return True

def solve(lst: list, l: list, size: int):
	summ = 0
	for i in range(len(lst)):
		summ += l[3][lst[i] - 1]
	return True if summ == size else False
h = N if N > M else M
lst = [1 for i in range(h)]
while True:
	if Next(lst, N, M):
		if solve(lst, l, size):
			print(lst)
	else:
		break