# https://www.acmicpc.net/problem/22864

# 한시간 일하면 피로도 +A
# B만큼 일을 할 수 있다
# 한시간을 쉰다면 피로도 -C > 0 B=B
# 피로도는 M을 넘지 않는다 M을 넘으면 fail
# 하루는 24시간


a, b, c, m = map(int, input().split())

f = 0  #피로도
w = 0  #처리하는 일
h = 0  #시간==24시간
while True:
    if h==24:
        print(w)
        break
    
    elif f >= 0 and f+a <= m and h < 24:
        f += a
        w += b
        h += 1
        print(f, w, h)   
    
    elif f+a > m:
        f -= c
        # w = 0
        h += 1
        print(f, h)
    
    elif a > m:
        print(0)
        break
    

