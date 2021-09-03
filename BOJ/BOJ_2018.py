# https://www.acmicpc.net/problem/2018 : 투 포인터

# 리스트의 연속하는 값의 합을 타겟값으로 구하는 경우의 가짓수를 출력


# cnt=0
# for i in range(1, n+1):
#     if cnt != 15:
#         cnt += i


# 연속되는수
# 15를 구한다면
# 홀수 일때 시작은 n//2 +1 부터
# 15
# 87         654321
#            7654321
# 654        321
# 54321

# 10을 구한다면
# 짝수 일때 시작은 n//2-1
# 10
# 4321


# cnt = 0
# max_num = odd  : n//2+1
#           even : n//2-1

    # elif n//2 != 0: #홀수 시작번호
    #     max_num = n//2 - 1    
    #     cal += max_num - 1    

# def even_num(n, cal, cnt):  #짝수 시작번호

#     if cal == n:
#         return cnt
#     else:
#         max_num = n//2 - 1 
#         cal += max_num
#     return even_num(n, cal, cnt+1, max_num-1)

# n = int(input())
# print(even_num(n, 0, 0))

# =====================================================================
# 입력 받은 숫자를 리스트에 넣어서 인덱싱 사용하면 시간초과나옴
# n =  int(input())

# nums=list(range(n, 0, -1))
# print(nums)
# start = 0
# end = 1
# cnt = 0
# while end <= n and start <=end:  #end가 끝까지 가고 start가 end만큼 가면
#     sum_nums = nums[start:end]
    
#     total = sum(sum_nums)
#     print(f'sum_num[{start}:{end}]')
#     print(total)

#     if total == n:
#         cnt += 1
#         end += 1
#     elif total < n:
#         end += 1
#     else:
#         start += 1

# print(cnt)


# n = int(input())

# start, end = 1, 2
# total = 3
# cnt = 0

# while end <= n and start <= end:
#     if total == n:
#         cnt += 1
#         start += 1
#         total -= start-1

#     elif total < n:
#         end += 1
#         total += end

#     else: # total > n
#         start += 1
#         total -= start-1
# print(cnt)

#시간 줄이는 법은 입력값 n은 무조건 포함하므로 cnt=1로 시작하고 
#탐색하는 범위를 
#홀수 일때는 n//2+1부터 시작하고
#짝수 일때는 n//2-1부터 시작하므로
#모두다 포함 할 수 있는 n//2+1까지 줄이면 된다 

#인덱스로 작동원리 한 번 보면 좀 더 직관적임
n = int(input())

start, end = 1, 2 # 입력 값이 15, 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15정렬된 리스트이기 때문에 값을 +1씩 하는걸로 
total = 3         # 순차적인 값들의 일정 합을 얻어낼 수 있음 시작이 1,2 이므로 토탈값은 3부터 시작
cnt = 1           # 처음에는 15부터 1까지 연속된 수를 돌면서 합을 구했는데
                  # 자기자신은 무조건 포함이므로 cnt=1부터 시작하고 
                  # 연속되는 값은 10이 입력이면 9876은 10이 연속하는 합이10이 될 수 없기 때문에 4~1까지 보면됨 n//2-1
                  #               15: 15 14 13 12 11 10 9//15가 될 수 없음 8부터 보면됨 n//2+1부터
                  # 둘을 모두 포함하는 n//2+1부터 보면 됨
while end <= n//2 + 1 and start <= end: #while문 탈출 조건 end가 탐색 끝 값까지 and start는 최대 end까지 두조건 모두 만족해야함
    if total == n:       #합이 타겟값이면 cnt +1, 시작값을 다음값부터 또 시작해야함 
        cnt += 1
        start += 1
        total -= start-1 #시작값이 앞으로 한칸 갔기 때문에 토탈값에서 스타트이전값을 빼줘야함

    elif total < n:       #합이 타겟보다 작으면 end +1씩 해가면서 total에 더해줌
        end += 1
        total += end

    else: # total > n    #total값이 타겟값보다 커도 스타트를 옮겨서 새로 카운팅을 시작해야함
        start += 1  
        total -= start-1    #total값도 위에서 와 같이 새로 시작하는 값을 첫값으로 더해줘야 하기 때문에 이전 시작값을 빼줘야함(시작이 3인 이유를 생각해 보면 됨)
print(cnt)