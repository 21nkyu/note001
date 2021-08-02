# 한 번에 운동기구 2개 선택가능
# 헬스장에 N개의 운동기구를 한번씩 사용하고 싶음
# 홀수개의 경우는 하나의 운동기구 사용
# 근손실 정도가 M을 넘지 않게
# N, M


N = int(input())
T = list(map(int, input().split()))
# if N%2 != 0:
big_M=[]
for i in T :
    for j in range(N):
        if i !=T[j]:
            print(f'{i} + {T[j]}', "=", i+T[j])
            comb = i + T[j]
            big_M.append(comb)
print(big_M)

sml_M = []
for comb_num in big_M:
    sml_M.append(big_M.count(comb_num))
    lss = max(sml_M)
M=[]
MM=[]
for k in range(len(big_M)):
    
    
    pair = [big_M[k], sml_M[k]]
    print(pair)
    M.append(pair)
for v in M:
    if v[1] == lss:
        MM.append(v[0])
print(MM)
print(min(MM))

import sys

N = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))

big_M=[]
for i in T :                        #T에 있는 원소 i
    for j in range(N):
        if i !=T[j]:                #자기 자신과 같은수 제거
            comb = i + T[j]         
            big_M.append(comb)      #big_M에 저장
cnt_M = []                          #big_M에 있는 원소의 수를 카운팅
for comb_num in big_M:
    cnt_M.append(big_M.count(comb_num))
    lss = max(cnt_M)
M=[]
MM=[]
for k in range(len(big_M)):
    pair = [big_M[k], sml_M[k]]
    M.append(pair)

for v in M:
    if v[1] == lss:
        MM.append(v[0])
print(min(MM))


import sys

N = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))

big_M=[]
for i in T :                        #T에 있는 원소 i
    for j in range(N):
        if i !=T[j]:                #자기 자신과 같은수 제거
            comb = i + T[j]         
            big_M.append(comb)      #big_M에 저장
set_M = list(set(big_M))            #big_M 중복제거
print("set_M:",set_M)
cnt_M= []                           #big_M에 있는 원소의 카운트를 담을 리스트

for j in range(len(set_M)):         #카운팅, 저장
    k = big_M.count(set_M[j])
    cnt_M.append(k)

print("cnt_M:", cnt_M)
lss = max(cnt_M)                    #원소를 카운팅한 값들중 가장 큰값// 이유는 comb(운동기구 2개 조합)가 1,2,3,4에 모두 하나씩 속해있어야한다.
pair_M = []                         #중복을 제거한 리스트 set_M에서 cnt_M한 카운팅한 값에 연결하여 comb(조합)값에 접근하는것이 잘 생각이 안남
for v in range(len(set_M)):         
    pair = [set_M[v], cnt_M[v]]     #pair_M 이중리스트 만듦
    pair_M.append(pair)
print("pair_M: ",pair_M)
M=[]                                
for w in pair_M:                    #그래서 그냥 리스트 안에 리스트 만들어서 반복문을 통해서 이중리스트에 접근해서 값을 뽑아냄.
    if w[1] == lss:                 
        M.append(w[0])
print("minimum of muscle loss:", min(M))



#예제 케이스가 몇개 더 있었다면 이딴 코드는 안짰을 거임 문제를 제대로 이해를 못하겠음.



