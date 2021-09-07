<<<<<<< HEAD
# https://www.acmicpc.net/problem/10448
=======
# https://www.acmicpc.net/problem/10448



# #Tn = 1000보다 작다
# for n in range(1000):
#     if n*(n+1)/2 <= 1001:
#         print(n, n*(n+1)/2)

# n = 45
# print(n, n*(n+1)/2)

tri = [int(n*(n+1)/2) for n in range(1, 45)] #총 Tn
nums = [0 for _ in range(1001)]              #count 해주기 위한 공간
# print(nums)
for i in tri:                               
    for j in tri:
        for k in tri:
            if i+j+k <= 1000:               #전체 탐색해서 1000보다 
                nums[i+j+k] = 1             #작으면 카운트 공간에 1을 넣어줌 여기에 기록된 인덱스와

t = int(input())
for _ in range(t):                          
    tt = int(input())                       
    print(nums[tt])                         #여기인덱스와 같음
>>>>>>> 8f8a41943fdf9d2ce96f1d75c9adbf76fcb6e00b
