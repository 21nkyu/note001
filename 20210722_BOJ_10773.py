#재현 정신없음 실수로 돈의 액수를 잘못 부름
#재현이는 잘못된 수를 부를때 마다 0을 외친다
#재현이 0을 외치면 재민이가 쓴 수를 지운다
#재민이가 모두 받아적은후 수의 합을 알고 싶어 한다.
#글만 보고 이해하기 어렵다

# 첫째줄에 정수 K가 주어진다
# K번 입력 받는다
# 입력 받는 수가 0일 경우 가장 최근에 쓴 수를 지운다
# 0이 아니면 받아적는다
# 0을 입력받으면 지울 수 있는 수가 있음을 보장 받는다

# 수를 입력 받는다
# 수만큼 반복 해서 입력을 받아서 리스트에 저장한다
# 입력받는 수가 0 이라면 0을 포함하여 그 뒤의 숫자 까지 즉 뒤에서 2개를 지운다
# 인덱싱을 사용해서 remove 할 것이다


import sys                                      #input을 사용하면 4800ms 정도 나온다 정답처리는 됨

K = int(sys.stdin.readline())                   #입력받을 수의 개수
number = []                                     #입력 받는 수를 저장할 리스트
for _ in range(K):                              #K번 반복해서 수를 입력을 받음
    input_num = int(sys.stdin.readline())       
    number.append(input_num)                    #입력 받은수를 number 리스트에 저장
    if input_num == 0:                          #조건 : 0을 입력 받으면 0앞에 입력받은 수를 지운다 즉 0 포함 2개를 지워 줘야한다.
        del number[-2:]                         #-2부터 끝까지 리스트의 수를 지워준다
   
result = sum(number)                            #리스트의 남은 값을 더해준다
print(result)                                   #결과를 출력한다.





import sys
K = int(sys.stdin.readline())
number = []
for _ in range(K):
    input_num = int(sys.stdin.readline())
    number.append(input_num)
    if input_num == 0:
        del number[-2:]
    print(number)
    
result = sum(number)
print("==========")
print(result)