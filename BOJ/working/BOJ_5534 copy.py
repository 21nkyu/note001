# https://www.acmicpc.net/problem/5534

# import sys
# input=sys.stdin.readlines

# n = int(input())
# target_sign = input()
# cnt = 0

# for _ in range(n):
#     input_sign = input()
#     if target_sign in input_sign:
#         cnt += 1
#     else:
        
#         # print(mm)
#         if input_sign[0] != target_sign[0]:
#             start_word = input_sign.find(target_sign[0])
#             new_sign = input_sign[ start_word: ]
#             for j in range(2, len(new_sign)):
#                 sign = []
#                 flag = 1
#                 for i in range(0, len(new_sign), j):
#                     sign.append(new_sign[i])
#                     sign1=''.join(sign)
#                     print(sign1)
#                     if target_sign in sign1:
#                         cnt += 1
#                         flag = 0
#                         break
#                 if flag == 0:
#                     break

        
              
        # else:
        #     while True:
        #         start_idx = 0
        #         end_idx = len(input())

        #         if start_idx >= end_idx:

                    
        #             for j in range(2, end_idx):
        #                 sign=sign[start_idx:]
        #                 flag = 1                      
        #                 for i in range(0, input_sign, j):
        #                     sign.append(sign[i])
        #                     sign1=''.join(sign)
        #                     if target_sign in sign1:
        #                         cnt += 1
        #                         flag = 0
        #                         start_idx +=1
        #                         break
        #                 if flag == 0:
        #                     start_idx +=1
        #                     break


                    
            
                
# print(cnt)


n, m, cnt = int(input()), input(), 0 

for _ in range(n):
    mm=input()
    if m in mm:
        cnt += 1
    else:
        s = mm.find(m[0])
        mmm = mm[s:]
        # print(mm)
        for j in range(2, len(mmm)//2):
            sign = []
            flag = 1
            for i in range(0, len(mmm), j):
                sign.append(mmm[i])
                sign1=''.join(sign)
                print(sign1)
                if m in sign1:
                    cnt += 1
                    flag = 0
                    break
            if flag == 0:
                break

print(cnt)