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
#아무생각없이 이런식으로 리스트를 이용해서 삭제하는 방법으로 풀었는데
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
#아무생각없이 이런식으로 리스트를 이용해서 삭제하는 방법으로 풀었는데 시간초과남 그래서 밑에 보니 해쉬테이블이라고함
#================================================

# 날로 먹으려고 조건에서 참가자가 중복허용이란 것을 보고도 set이용했는데 역시 안됨 
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
                                #비어있는 dict에서 시작함
for i in range(n):              #참가선수가 dict안에 없으면 key(선수) : value(값) value +1
    if run[i] not in check:
        check[run[i]] = 1

    else:
        cnt = check[run[i]]     #cnt는 현재값을 구하기 위한 값
        check[run[i]] = cnt + 1 #현재값 + 1, 중복이라면 a : 2 가 돼있음
# 전체 참가 {key(선수1) : value(선수1), key(선수2) : value(선수2).........} 

# 완주 선수는 value -1 해줌
for i in range(n-1):
    cnt = check[fin[i]]
    check[fin[i]] = cnt - 1

# 이렇게 해서 value값이 정리된 테이블???에서 
# 참가하면 +1 완주하면 -1 이므로 value에 +1이 있는 친구가 완주하지 못한 친구임
# 그것을 확인하는 것이 마지막 코드임
for key in check:
    if check[key] == 1:
        print(key)
        break