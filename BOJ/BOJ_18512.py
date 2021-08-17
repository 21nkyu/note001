# https://www.acmicpc.net/problem/18512

# 두 학생 A, B일직선상 같은 방향으로 멀리뛰기
# A : 한번에 X미터
# B : 한번에 Y미터
# 두 학생의 시작 지점과 X, Y 정보가 주어짐
# 공통으로 지나는 지점 중 시작점에서 가장 가까운 지점을 찾는 프로그램

# ex)
# A : 한번에 10미터뜀, 시작점 30m, 5번 뜀
# B : 한번에 12미터뜀, 시작점  8m, 6번 뜀

# X, Y, P_1, P_2 =  map(int, input().split())
# V = set([P_1 + 10*i for i in range(1, X+1)]) 
# W = set([P_2 + 12*j for j in range(1, Y+1)])
# # print(V)
# # print(W)
# Z = list(V & W)
# # if len(Z) > 0:
# #     print(min(Z))
# # else:
# #     print(-1)
# # print(Z)
# Z = []
# if V in W:
#     Z.append(V)
#     print(min(Z))
# else:
#     print(-1)



X, Y, P_1, P_2 =  map(int, input().split())
V = set([P_1 + X*i for i in range(1000)]) 
W = set([P_2 + Y*j for j in range(1000)])
# print(V)
# print(W)
Z = list(V & W)
# print(min(Z))
if len(Z) > 0:
    print(min(Z))
else:
    print(-1)


X, Y, P_1, P_2 =  map(int, input().split())

V = set([P_1 + X*i for i in range(1000)]) 
W = set([P_2 + Y*j for j in range(1000)])

Z = list(V & W)
if len(Z) > 0:
    print(min(Z))
else:
    print(-1)