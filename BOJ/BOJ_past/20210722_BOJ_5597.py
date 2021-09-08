
# 문제요약
# 1. student = 30 명 
# 2. 1번 ~30번 까지 출석번호
# 3. 28명이 과제 제출
# 4. 제출하지 않은 2명의 출석번호 오름차순 출력 2명을 한줄에 하나씩 출력
# 5. 입력은 한줄에 하나씩
# 6. 출석번호 중복없다


# 사용할 방법
# 전체 학생 리스트 만들기
# 입력 28번 받아서 제출 학생 리스트 만들기
# 제출 학생 리스트의 원소가 전체 학생 리스트를 원소를 순차적으로 비교해서 remove를 통해 삭제 하는 방법을 사용할 것임

students = [i for i in range(1, 31)]                        #전체 학생 리스트

for _ in range(28):                                         #입력 28번
    submitted_student = int(input())                        #수학적 계산을 해야하기 때문에 int형태로
    submitted_students = [submitted_student]                #pycham에서 이렇게 쓰라고 알려줌
    #submitted_students = []
    #submitted_students.append(submitted_student)
    for student_idx in range(len(submitted_students)):      #제출한 학생이 있는 리스트의 인덱스를 통해서 접근 하였음                                         
        stdt = submitted_students[student_idx]
        students.remove(stdt)                               #전체 학생 리스트에서 제출 학생[인덱스]를 통해 제출 학생 원소에 접근하여 remove를 하였음
print("=========")        
print(students[0])              #print(min(students))       #전체 학생 리스트는 항상 2개가 남고 오름차순이기 때문에 인덱스를 사용하였음
print(students[1])              #print(max(students))       #min, max를 사용해도 무방함
