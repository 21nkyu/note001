T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    if a%10 == 1:
        print(1)
    
    if a%10 == 4 or a%10 == 9:
        if b%2 == 1:
            print(a%10)
        elif b%2 == 0:
            n = (a%10)**2
            print(str(n)[-1])
    if a%10 == 0:
        print(10)
    
    if a%10==2 or a%10==3 or a%10==7 or a%10==8:                     
        if b%4 == 0:
            m = (a%10)**4
            print(str(m)[-1])
        elif b%4 != 0:
            k = (a%10)**(b%4)
            print(str(k)[-1])
    
    if a%10 == 5 or a%10 ==6:
        print(a%10)



#=========================================

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    i = a**b
    print(str(i)[-1])

