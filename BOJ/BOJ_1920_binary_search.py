# https://www.acmicpc.net/problem/1920

n = int(input())
n_list = sorted(list(map(int, input().split())))

m = int(input())
for target_num in map(int, input().split()):
    
    start_idx  = 0
    end_idx    = n-1
    get_target = 0
    
    while end_idx <= n-1 and end_idx >= start_idx:
        mid_idx = (start_idx + end_idx) // 2
        if n_list[mid_idx] > target_num: # s t m e => s t e(move) m
            end_idx = mid_idx - 1
        elif n_list[mid_idx] < target_num: #s m t e => m s(move) t e
            start_idx = mid_idx + 1
        else: # t = m
            get_target = 1
            break
    print(get_target)
