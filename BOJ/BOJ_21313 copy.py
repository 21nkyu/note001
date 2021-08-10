
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
