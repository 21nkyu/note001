조건 집합 K의 원소로 구성된 가장 큰 수
K의 원소는 1~9까지 자연수
첫째줄 N 기준이 되는수 K는 원소의 개수(1<= K<=3)
N보다 작거나 같은 자연수 중에서 K의 원소로만 구성된 가장 큰 수



N, K =map(int, input().split())

K_list = map(int, input().split())

for i in K_list:
    for j in K_list:
        for k in K_list:
            
        