# https://www.acmicpc.net/problem/1620

n, m = map(int, input().split())

input_list = []

for _ in range(n+m):
    name = input()
    input_list.append(name)

pkm_list = input_list[0:26]
trgt_list = input_list[-5:]
# print(pkm_list)
# print("================")
print(trgt_list)
books = {}
for idx, pkm in enumerate(pkm_list, start=1):
    books[pkm] = idx
# print(books)
# print(i_books)
for j in trgt_list:
    if j.isdigit():
        print(pkm_list[int(j+1)])
    else:
        print(books[j])
# print(rvs_books['Raichu'])


