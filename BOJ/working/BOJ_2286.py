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
    if h==24:                               #하루 = 24시간
        print(w)                            #일 완료
        break
    
    elif f >= 0 and f+a <= m and h < 24:    #피로도, 다음에 누적 피로도, 시간 
        f += a                              #세가진 조건을 만족하면 피로도+ 처리하는일+ 시간+
        w += b
        h += 1
        print(f, w, h)   
    
    elif f+a > m:                           #다음 피로도가 피로도상한m 보다 크면              
        f -= c                              #이전 피로도 -휴식피로도
        # w += 0                            #일은 += 0
        h += 1                              #시간증가
        print(f, h)
    
    elif a > m:                             #피로도가 피로도 상산을 초과하면 0
        print(0)
        break
    

