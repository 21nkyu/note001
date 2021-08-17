# https://www.acmicpc.net/problem/1193

x = int(input())
box = 1
limit = 1        
while limit < x:  #limit가 x보다 커지면 
    box += 1          #1+1 2+1 3+1 4 +1   
    limit += box      #1+2 3+3 6+4 10+5
loc = x - (limit - box)  # 15-5 = 10
box_total = box+1
# print(box)
# print(limit)

if box%2 == 0:              #짝수 정
    up = loc
    down = box_total - loc
else:                       #홀수 역
    up = box_total - loc
    down = loc 

print(f'{up}/{down}')



#시간초과 메모리초과=========================================
# 0 ==============================================

x=int(input())

numer = []
while True:    
    for i in range(0, x+1):
        # print(f'i :{i}')
        if i%2==0:
            for j in range(1, i+1):
                numer.append(j)
                # print(f'j : {j}')
        elif i%2!=0:
            for k in range(i, 0, -1):
                numer.append(k)
                # print(f'k : {k}')            
    len(numer) == 14
    # print(numer)
    # print(numer[x-1]) #분자    
    break   

denomi=[]
while True:    
    for i in range(0, x+1):
        # print(f'i :{i}')
        if i%2!=0:
            for j in range(1, i+1):
                denomi.append(j)
                # print(f'j : {j}')
        elif i%2==0:
            for k in range(i, 0, -1):
                denomi.append(k)
                # print(f'k : {k}')            
    len(denomi) == 14
    # print(denomi)
    # print(denomi[x-1]) #분자
    break

print(numer[x-1], denomi[x-1])

print(str(numer[x-1])+'/'+str(denomi[x-1]))            


            # if len(numer) == 14:
            #     break


# for i in range(1, 100):
#     if i // 2 == 0:
#         print(i)
        # for j in range(1, i+1): 
        #     numer.append(j)
    # else:
    #     for k in range(i+1, 0, -1): 
    #         numer.append(k)

        
        # print(j)
        # print[x-1]


# x=int(input())
# numer = [
#     j 
#     for i in range(1, x+1) 
#     if i//2==0 
#     for j in range(1, i+1)#분자
#     if i//2!=0
#     for j in range(i+1, 0, -1)#분자
#     ]
# print(numer)
# # print(numer[x-1])

# 1================================================================
x=int(input())
cnt=0
ul = []
array=[]
for i in range(1, x+1):
    cnt += i
    if cnt // x == 1:
        if len(ul) == 0:
            ul.append(cnt)
            for j in range(1, i+1):                    
                array.append(j)            

if ul[0] % 2 == 1:
    print(f'{array[ul[0]-x]}/{array[-1]+1 - array[ul[0]-x]}')
else:
    print(f'{array[-((ul[0]-x)+1)]}/{array[-1]+1 - array[-((ul[0]-x) +1)]}')

# 2=================================================================================

x=int(input())
cnt=0
ul = []
for i in range(1, x+1):
    cnt += i
    # print(f'cnt : {cnt}')
    # print(f'i : {i}')
    array=[]
    if cnt // x == 1:
        # print(f'divided : {cnt//x}')
        if len(ul) == 0:
            ul.append(cnt)
            print(ul)
            if cnt % 2 == 1:
                for j in range(1, i+1):                    
                    array.append(j)
                    print(j)
                print(f'{array[cnt-x]}/{array[-1]+1 - array[cnt-x]}')
            if cnt % 2 == 0:
                for j in range(1, i+1):
                    array.append(j)
                    print(array)
                print(f'{array[-((cnt-x)+1)]}/{array[-1]+1 - array[-((cnt-x) +1)]}')


# 3??????????????====================================================================

x=int(input())

def cal(x):
    array = []
    while True:        
        for i in range(0, x):
            c_o_l = []
            if i%2==0:            
                for j in range(1, i+1):
                    # array.append(j)
                    c_o_l.append(i)           
            if i%2!=0:             
                for k in range(i, 0, -1):
                    # array.append(k)
                    c_o_l.append(i)
            if len(array) >= x:
                print(c_o_l)
                print(array)
                return array, c_o_l

array, c_o_l = cal(x)


if x == 1:
    print(f'{1}/{1}')
if x == 2:
    print(f'{1}/{2}')
else:
    print(f'{array[x-1]}/{max(c_o_l)+1-array[x-1]}')

