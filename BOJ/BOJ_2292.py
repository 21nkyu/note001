# # https://www.acmicpc.net/problem/2292

# #    2      3         4         5
# # 1 2~7(6) 8~19(12) 20~37(18) 38~61(24)

# T = int(input())

# room = 1
# limit = 1
# while T > limit:
#     limit += 6*room #1 1+6*1=7 7+6*2=19 19+6*3=37
#     room += 1       #1       2        3         4
# print(room)


T = int(input())

room = 1
limit = 1
while T > limit:
    limit += 6*room
    room += 1
    print(room, limit)       
print(room)