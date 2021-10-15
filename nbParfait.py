import sys

n = int(sys.argv[1])
s = 0
for i in range(1, n):
	if (n%i == 0):
		s += i
if (n == s):
	print(f"Le nombre {n} est parfait")
else:
	print(f"Le nombre {n} n'est pas parfait")
