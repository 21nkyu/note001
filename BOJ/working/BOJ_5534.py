# # https://www.acmicpc.net/problem/5534


# n = int(input())
# target_sign = input()
# cnt = 0

# for _ in range(n):
#     input_sign = input()
#     if target_sign in input_sign:
#         cnt += 1
#     else:
#         for j in range(2, len(input_sign)):
#                 start_idx = 0
#                 s1_idx = 0
#                 end_idx = len(input_sign)
#                 new_sign = input_sign[s1_idx:] 
#                 if start_idx == end_idx:
#                     break      
#                 else:
#                     sign = []
#                     flag = 1
#                     for i in range(0, len(new_sign), j):
#                         sign.append(new_sign[i])
#                         sign1=''.join(sign)
#                         print(sign1)
#                         if target_sign in sign1:
#                             cnt += 1
#                             flag = 0                            
#                             break
#                         else:
#                             start_idx += 1
#                             s1_idx += 1
#                     if flag == 0:
#                         start_idx += 1
#                         s1_idx += 1   
#                         break
                        

                        
# print(cnt)


# n = int(input())
# target_sign = input()
# cnt = 0

# for _ in range(n):
#     input_sign = input()
#     if target_sign in input_sign:
#         cnt += 1
#     else:

#         # print(mm)
#         if n[0] != target_sign[0]:
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
#         else:
#             for j in range(2, len(input_sign)):
#                 sign = []
#                 flag = 1
#             for i in range(0, len(input_sign), j):
#                 sign.append(input_sign[i])
#                 sign1=''.join(sign)
#                 print(sign1)
#                 if target_sign in sign1:
#                     cnt += 1
#                     flag = 0
#                     break
#             if flag == 0:
#                 break

# print(cnt)



# print(cnt)


#==============================================
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