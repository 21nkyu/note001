# https://www.acmicpc.net/problem/10546 : 해쉬 테이블
# 딕셔너리 벨류값을 조절해서 원하는 결과 얻어내기

# n = int(input())

# # r_list = set([input() for _ in range(n)])
# # f_list = set([input() for _ in range(n-1)])
# # print(r_list | f_list)
# all=[]
# for _ in range(n+n-1):
#     all.append(input())


# r_list = all[0:n]  #['leo', 'kiki', 'eden']
# f_list = all[n:]   #['eden', 'kiki']

# # print(r_list, f_list)
# print(len(f_list))

# # for i in range(len(f_list)):
# #     if f_list[i] in r_list:
# #         del f_list[i]
# # print(r_list)

#================================================


# import sys

# n = int(sys.stdin.readline().strip())

# all=[]

# for _ in range(n+n-1):
#     all.append(sys.stdin.readline().strip())

# r_list = all[0:n]
# f_list = all[n:]

# # for i in f_list:
# #     if i in r_list:
# #         r_list.remove(i)
# # print(r_list)

#================================================

# if len(set(r_list)) == len(set(f_list)):
#     for i in f_list:
#         if i in r_list:
#             r_list.remove(i)
#     print(r_list)
    
# else:   
#     print(list(set(r_list) - set(f_list)))

#================================================

# n = int(input())

# run = [input() for _ in range(n)]
# fin = [input() for _ in range(n-1)]
# check = {}

# for i in range(n):
#     if run[i] not in check:
#         check[run[i]] = 1
#         print('for1 if:', check)
#         print("=============================")
#     else:
#         cnt = check[run[i]]
#         print('else cnt:',cnt)
#         check[run[i]] = cnt + 1
#         print('for1 else:',check)
#         print("=============================")
# for i in range(n-1):
#     print(fin[i])
#     cnt = check[fin[i]]
#     print('for2 cnt:', cnt)
#     check[fin[i]] = cnt - 1
#     print('for2:',check)
#     print("=============================")
# for key in check:
#     if check[key] == 1:
#         print(key)

#================================================
import sys
n = int(input())

run = [sys.stdin.readline().strip() for _ in range(n)]
fin = [sys.stdin.readline().strip() for _ in range(n-1)]
check = {}

for i in range(n):
    if run[i] not in check:
        check[run[i]] = 1

    else:
        cnt = check[run[i]]
        check[run[i]] = cnt + 1

for i in range(n-1):
    cnt = check[fin[i]]
    check[fin[i]] = cnt - 1

for key in check:
    if check[key] == 1:
        print(key)
        break