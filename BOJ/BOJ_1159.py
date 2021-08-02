# 테스트 케이스 입력받음
# 테스트 케이스 만큼 선수이름 입력받음
# 5명 이상이면 경기를 하고
# 5명 이하면 기권
# 5명의 기준은 선수이름의 첫글자의 개수
# 같은 성이5명 이상인 경우가 여러개이면 사전순으로 출력

# 입력받은 선수이름의 첫글자 까지만 번위를 설정해 리스트에 담음
# 담긴 첫글자의 수를 세기는데 인덱스로 사용하기 위해 set으로 중복제거
# 사전순 출력 이기 때문에 첫글자가 담긴 리스트 sort
# 중복 제거한 리스트의 인덱스로 모든 성이 담긴 리스트에 있는 첫글자를 count해서 
# 첫글자가 같은 선수가 5명 이상이면 player리스트에 담음
# join을 사용하여 리스트의 원소를 붙여서 출력
# 리스트가 비어있다면 기권


N = int(input())
first = []                          #첫글자가 모두 담긴 리스트
for _  in range(N):
    names = input()
    for i in range(1):              #이름의 범위를 0으로 제한한
        first.append(names[i])      #첫글자를 리스트에 담음

set_first  = list(set(first))       #set중복제거해서 리스트로 변환
players=[]                          #첫글자가 같은 선수가 5명 이상이면 담는 리스트
players.sort()                      #사전순 sort
for i in set_first:                 #중복 제거된 성을 인덱스로 사용함
    if first.count(i) >= 5:         #5명 이상이면
        players.append(i)           #players에 저장
if len(players) == 0:               #5명 이상이 없으면 리스트에 담기지 않음
    print("PREDAJA")                #기권
print(''.join(players))             #첫글자가 5명 이상인 선수가 있다면 join으로 comma없애고 출력



