# 정수 x는 각 자리가 등차수열?
# 입력 1000보다 작거나 같은 자연수 n
# 1보다 크거나 같고 n보다 작거나 같은 한수의 개수 출력

# 110의 한수가 99
# 11개
# 일단 1~10이 한수인지 판별하는 코드

# def num(n):
#     n = [i for i in range(n)]
#     for j in str(range(1, len(n)+1)):
#         for k in range(1, len(j)-1):
#             j[k] - j[k+1]
#     return 

# num(10)
        
# number_set = set(range(1, 10001))
# self_num_set = set()

# for i in range(1, 10001):
#     for j in str(i):
#         i += int(j)
#         self_num_set.add(i)
# answer_set = number_set - self_num_set

# for i in sorted(answer_set):
#     print(i)



# n = int(input())
# def x(n):
#     for i in str(range(1, n+1)):
#         for j in (range(i)):
   

 
for i in range(1, 10+1):
    cnt = 0   
    box = []
    box.append(str(i))
    for j in range(len(box)-1):
        check=[]
        check.append(int(box(j))-int(box(j+1)))
        for k in range(0, len(check)-1):
            if check[k] == check[k+1]:
                cnt += 1
            elif len(check) <= 1:
                cnt += 1
    print(cnt)



