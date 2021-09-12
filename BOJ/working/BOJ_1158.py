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
