# https://www.acmicpc.net/problem/2869

# a, b, v = map(int, input().split())

a,b,v = map(int, input().split())



# if a-b == 1:
#     print(v-a+1)
# elif (v-a)%(a-b) + a >= v:
#     print(((v-a)%(a-b)) +1)
# elif (v-a)%(a-b) + a < v:
#     print(((v-a)//(a-b)) +2)
# elif (v-a)%(a-b)==0:
#     print(((v-a)//(a-b)) +1)

#=====================================

# a,b,v = map(int, input().split())

# if a-b == 1:
#     print(v-a+1)
# elif (v%(a-b)) == 0:
#     print(v//(a-b))
# else: 
#     print(v//(a-b)+1)




# vh=0 #h >= v stop
# upcnt = 0
# while True:
#     vh += a
#     # print('vh', vh) 
#     if vh >=v:
#         upcnt += 1
#         print(upcnt)
#         break
    
#     vh -= b
#     # print('vh', vh)
#     upcnt += 1
#     # print('upcnt', upcnt)

