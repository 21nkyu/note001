# https://www.acmicpc.net/problem/1158

# 1부터 n번까지 n명의 사람이 원 = 원형큐
# 양의 정수 k
# 순서대로 k번째 사람을 제거한다 = k-1번째 까지 맨 뒤 인덱스에 붙는다
# 한 사람이 제거 되면 다음 k번재 제거


from collections import deque

n, k = map(int, input().split()) # n명 k번째

x, y=deque(range(1, n+1)), [] # x = n명이 들어있는 리스트, y = [] 빈리스트 -> x에서 pop해서 y에 append
while True:
    if len(x) > 0:            # x에 원소가 남아 있으면
        x.rotate(-(k-1))
        xx = x.popleft()
        y.append(xx)
    elif len(x) == 0:         # x에 원소가 남아 있지 않으면
        y_list = str(y)[1:-1] # 다른방 법이 생각이 안나서 인덱싱으로 대괄호 제거
        print(f"<{y_list}>")
        break

#======================================================

# from collections import deque

# n, k = map(int, input().split())

# x, y=deque(range(1, n+1)), []
# while True:
#     if len(x) > 0 and k%2!=0:
#         x.rotate(-(k-1))
#         xx = x.popleft()
#         y.append(xx)
    
#     elif len(x) > 0 and k%2==0:
#         x.rotate(-(k-1))
#         xxx = x.popleft()
#         y.append(xxx)
#         if len(x) == 2:
#             y.append(x.pop())
#     elif len(x) == 0:
#         print('<{}>'.format(y))
#         break


#=========================================================

# from collections import deque

# n, k = map(int, input().split())

# x, y=deque(range(1, n+1)), []
# while True:
#     if len(x) > 0:
#         x.rotate(-(k-1))
#         print(list(x))
#         xx = x.popleft()
#         y.append(xx)
#         print(y)
#     elif len(x) == 0:
#         print(y)
#         break




#======================================================






# from collections import deque

# # x =  deque([range(1, 8)])

# n, k = map(int, input().split())

# x=deque(range(1, n+1))
# print(x)
# print(len(x))
# y=[]
# while True:
#     if len(x) > 0:
#         x.rotate(-(k-1))
#         print(list(x))
#         xx = x.popleft()
#         y.append(xx)
#         print(y)
#     # elif len(x) <= k-1 and len(x) > 0:
#     #     x.rotate(-1)
#     #     print(x)
#     #     xxx=x.popleft()
#     #     y.append(xxx)
#         # print(y)
#     elif len(x) == 0:
#         print(y)
#         break




# x=[1,2]
# print(x*2)
