# https://www.acmicpc.net/problem/3009

x,y,z=[],[],[]
for _ in range(3):
    n, m = map(int, input().split())
    x.append(n)
    y.append(m)
for i in x:
    if x.count(i)==1:
        z.append(i)
for i in y:
    if y.count(i)==1:
        z.append(i)

print(*z)
# for i in z:
#     print(i, end=' ')


#=====================================
# x,y,z=[],[],[]
# for _ in range(3):
#     n, m = map(int, input().split())
#     x.append(n)
#     y.append(m)
# for i in x:
#     if x.count(i)==1:
#         z.append(i)
# for i in y:
#     if y.count(i)==1:
#         z.append(i)
# # print(x)
# # print(y)
# print(*z)
