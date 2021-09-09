# https://www.acmicpc.net/problem/2751

# n 개 수가 주어짐 

# 목표 오름차순정렬

# 첫 줄 n개
# 둘째줄부터 n개의 줄에 수가 주어짐 세로로

# 출력 오름차순 정렬한 결과를 한 줄에 하나씩 출력한다?


n=int(input())
n_list=[int(input()) for _ in range(n)]
# print(n_list)
nn_list = []
# 인덱스 2개 관리
mid_idx = len(n_list) //2
left_idx = 0 
right_idx = mid_idx +1

while left_idx <= mid_idx and right_idx <= n-1:
    # nn_list = []
    if n_list[left_idx] < n_list[right_idx]:
        nn_list.append(n_list[left_idx])
        left_idx += 1
    elif n_list[left_idx] > n_list[right_idx]:
        nn_list.append(n_list[right_idx])
        right_idx+=1
    else:
        break
print(nn_list, end='\n')


# 문제해결 정렬이 된다 = 값이 하나일때 = if start_idx == end_idx return 값이 하나짜리 리스트가 넘어간다는 것을 기억해라
# merge_sort과정에서
# combined_list=[]
# while f[fidx] <=len(f) or이냐 and냐 b[bidx]<=len(b) and or 모두 동작하지 않음


# f<b
# 작은값을 넣어지고
# 어펜드
# 작은값의 리스트 인덱스 +1
# 반대의 경우도 똑같음

# 프론트를 다 넣으면 백에서 못넣은 값들이 남아있을수도 있다

# 백이든 프론트든 하나는 끝났다 하나는 빈리스트가 나온다
# 나머지 하나의 남은 리스트를 붙여준다
# print(combined_list = combined_list +f[fidx:] +b[bidx:]) 동작을 볼 수 있음
# return combined_list = combined_list +f[fidx:] +b[bidx:]
# 탑 다운 방식