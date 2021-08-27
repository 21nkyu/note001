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



# X, Y, P1, P2 = map(int, input().split())

# # P1+X*i == P2+Y*j
# i, j = 0
# while True:
#     V =P1+X*i
#     W =P2*Y*j
#     if V == W:
#         print(i, j) 
# 2차 방정식인데 식이 아무리해도 식이 하나밖에 안나와서 원래 코드로 돌아옴



X, Y, P_1, P_2 =  map(int, input().split())

V = set([P_1 + X*i for i in range(1000)]) #이 범위를 가장 멀게 잡는다고 생각하고 
W = set([P_2 + Y*j for j in range(1000)]) #100m에서 뛰기 시작하고 한 스텝에 100m뛴다고 생각하고 1000번정도 점프하면 되자 않겠나??
                                          #하고 그냥 1000 넣으니 맞다고 해줌.. ㄳㄳ
Z = list(V & W)                           #교집합을 구하고
if len(Z) > 0:                            #Z에 원소가 있으면 
    print(min(Z))                         #가작 작은 값은 출력
else:                                     #1000번 점프해도 일치하는 수가 없으면
    print(-1)                             #-1출력
                                          #range에 근거가 될만한 힌트를 못찾았음. 
                                          #다음에 이런문제 만나면 적당한 선에서 범위를 주고 맞을때 까지 돌려봐야겠다. 혹시 이번처럼 맞을지도 모르니.