# https://www.acmicpc.net/problem/1158

# 1부터 n번까지 n명의 사람이 원
# 양의 정수 k
# 순서대로 k번째 사람을 제거한다
# 한 사람이 제거 되면 다음 k번재 제거


from collections import deque

n, k = map(int, input().split())

x, y=deque(range(1, n+1)), []
while True:
    if len(x) > 0:
        x.rotate(-(k-1))
        xx = x.popleft()
        y.append(xx)
    elif len(x) == 0:
        y_list = str(y)[1:-1]
        print(f"<{y_list}>")
        break