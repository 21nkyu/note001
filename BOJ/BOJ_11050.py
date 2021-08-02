n, r = map(int, input().split())

nmrtr = 1
f_dnmntr = 1
b_dnmntr = 1

for i in range(n, 0, -1):
    nmrtr *= i

for j in range(r, 0, -1):
    f_dnmntr *= j

for k in range(n-r, 0, -1):
    b_dnmntr *= k

bi_coef = nmrtr / (f_dnmntr*b_dnmntr)

print(int(bi_coef))