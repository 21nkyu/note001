# https://www.acmicpc.net/problem/2869

a, b, v = map(int, input().split())

# day = v//(a+b)

# def up(a,b,v):
#     return(v-a+1)

# print(up(a,b,v))

if ((v-a)/(a-b)) + a >= v:
    print((v//(a-b)) - 1)
elif ((v-a)/(a-b)) + a < v:
    print((v//(a-b)) + 1)
