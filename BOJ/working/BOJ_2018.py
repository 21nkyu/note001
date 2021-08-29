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
#홀수 일때는 n//2-1부터 시작하고
#짝수 일때는 n//2+1부터 시작하므로
#모두다 포함 할 수 있는 n//2+1까지 줄이면 된다 

n = int(input())

start, end = 1, 2
total = 3
cnt = 1

while end <= n//2 + 1 and start <= end:
    if total == n:
        cnt += 1
        start += 1
        total -= start-1

    elif total < n:
        end += 1
        total += end

    else: # total > n
        start += 1
        total -= start-1
print(cnt)