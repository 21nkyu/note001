# https://www.acmicpc.net/problem/21313


# 문어의 손은 1~8까지 고유번호를 가지고 있음
## 가운데 문어는 좌측 문어와 우측 문어와 손을 잡고 있음
### 문어의 손은 고유 번호를 가지고 있기 때문에 좌측문어와 잡은손과 우측문어와 잡은 손은 다른번호를 가진 손임
#### 가장작은 수열을 만들어야함  
N = int(input())

if N%2 == 0:
    b = [j for j in range(1, 3)]
    print(*b*int(N//2))
    
else:
    d = [i for i in range(1, 3)]
    print(*d*int(N//2), 3)

## 1 2 구하는 배열이 반복이길래 함수로 한번 만들어봄...
### 병국이가 알려준 print(*) 사용해서 리스트에 안넣고 바로 프린트로 뽑아내면서 사용해봄
def array():
    a = [i for i in range(1,3)]
    return a

N = int(input())

if N%2 == 0:
    print(*array()*int(N//2))
    
else:
    print(*array()*int(N//2), 3)
