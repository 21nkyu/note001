#1. 문자열
#2. 입력받은 수를 10으로 나눈 나머지와 10으로 나눈 몫을 계속 더한다


#2

def d(n):
    result = n                             
    while n != 0:                       
        result += n%10
        n =  n//10
        return result

not_self_num = []
for i in list(range(1, 10)):
    not_self_num.append(d(i))
    if i not in not_self_num:
        print(i)


#2-1

##셀프넘버 만드는 함수
def d(n):
    recycle_number = int(n)             #입력받은 수 = r_n
    for i in list(str(n)):              #문자열 -> 리스트 -> 원소를 모두 더한다.
        recycle_number += int(i)
    return recycle_number               #r_n 리턴 하면 다시 r_n는 갱신
not_self_num = []
for i in list(range(1, 10001)):         #1~10001 까지 리스트 생성하면서 1~10001까지 원소 하나하나 호출
    not_self_num.append(d(i))
    if i not in not_self_num:
        print(i)

#2-2 /2-1을 다르게 표현

def d(n):
    a = list(str(n))
    recycle_number = 0
    for i in range(len(a)):
        recycle_number += int(a(i))
    return n+recycle_number


#3 set

number_set = set(range(1, 10001))
not_self_num_set = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
        not_self_num_set.add(i)
self_num_set = number_set - not_self_num_set

for i in sorted(self_num_set):
    print(i)
