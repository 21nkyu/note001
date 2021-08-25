# https://www.acmicpc.net/problem/1913

N=int(input())
# hold=10
# cnt = 1
# row = []
# for i in range(1, N+1):
#     row.append(i)
# for _ in range(N):
#     print(row, end='\n')
#     cnt+=1
#     hold *= cnt
array=[]

for i in range(1, N+1):
    for j in range(1, N+1):
        # print(i, j)
        array.append((i, j))
# print(array)



start_n = 0
end_n = len(array)
div_n = N
for k in range(start_n, len(array)+div_n, div_n):
    print_out = array[start_n:start_n+div_n]
    if print_out != []:
        print(print_out)
        start_n += div_n


# idx_array = []
# for idx, path in zip(range(1, 10), array):
#     print(idx, path)
#     idx_array.append((idx, path))


# start_n = 0
# end_n = len(idx_array)
# div_n = N
# for k in range(start_n, len(array)+div_n, div_n):
#     print_out = idx_array[start_n:start_n+div_n]
#     if print_out != []:
#         print(print_out)
#         start_n += div_n
# print(f'{idx_array[8]},{idx_array[7]}')


#     print(array)
# for l in range(0,N):
#     print(snail_path[l], end='\n')



dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
def snail(center):                      # 가운댓 값을 받아 달팽이 함수를 만든다.
    cnt = 1                             # 달팽이가 움직이면서 쓰일 변수를 만든다. 시작은 1부터 시작
    repeat = 2                          # 규칙을 보면 1칸씩 2번, 2칸씩 2번, 3칸씩 3번 이런 규칙을 가진다.
    length = 1                          # repeat이 반복되는 동안 길이만큼 이동한다.
    x, y = center                       # 시작지점
    i = 0                               # 방향을 정해준다.
    graph[x][y] = cnt                   # 가운댓값은 1로 넣어준다.
    loc = [N//2+1, N//2+1]              # 찾아야하는 좌표를 저장하기 위한 리스트 1일때는 찾지 않기때문에 우선적으로 넣어준다.
    while cnt < N**2:                   # N*N 크기의 2차행렬이므로 그 이상이 되면 종료한다.
        for _ in range(length):         # 길이만큼 그 방향으로 진행한다.
            x, y = x + dx[i], y + dy[i] # 새로운 좌표를 저장한다.
            cnt += 1                    # 새로운 좌표에 저장할 값
            if cnt == target:           # 만약 타겟 넘버라면
                loc = [x+1, y+1]        # 저장한다.
            if cnt > N**2:              # 만약 cnt값이 N*N을 넘으면 종료한다.
                break
            graph[x][y] = cnt           # 2차원 행렬의 새로운 좌표에 값을 넣어준다.
        else:                           # for문이 정상적으로 종료되면
            i = (i+1)%4                 # 방향에 1을 더하고
            repeat -= 1                 # 반복횟수를 1 빼준다.
        if repeat == 0:                 # 반복횟수가 0이되면
            length += 1                 # 길이를 +1 해주고
            repeat = 2                  # 반복횟수를 초기화해준다.
    return loc                          # 종료되면 타겟넘버의 좌표를 출력해준다.
N = int(input())        # 표의 크기를 받는다
target = int(input())   # 찾아야 하는 숫자를 받아온다.
graph = [[0 for _ in range(N)] for _ in range(N)]   # N*N 크기의 2차원 행렬을 만들어준다.
result = snail((N//2, N//2))                        # 달팽이 함수를 실행한다.
for i in graph:                                     # 그래프를 출력해준다.
    print(*i)
print(*result)                                      # 타겟 넘버의 좌표로 출력해준다.