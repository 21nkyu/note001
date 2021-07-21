# 1. student = 30 명 
# 2. 1번 ~30번 까지 출석번호
# 3. 28명이 과제 제출
# 4. 제출하지 않은 2명의 출석번호 오름차순 출력
# 5. 입력은 한줄에 하나씩
# 6. 출석번호 중복없다
# 7. 2명을 한줄에 하나씩 출력

# 사용할 방법
# 전체 학생 리스트 만들기
# 입력 28번 받아서 제출 학생 리스트 만들기
# 제출 학생 리스트의 원소가 전체 학생 리스트를 원소를 순차적으로  비교하며 remove를 통해 삭제 하는 방법을 사용할 것임

 #전체 학생 리스트 #학생 번호는 1번 부터, 시작숫자에 유의

students = [i for i in range(1, 31)]

for _ in range(28):
    submited_student = int(input())
    submited_students = []
    submited_students.append(submited_student)
    for student_idx in range(len(submited_students)):
        students.remove(submited_student[student_idx])
        
print(students[0])
print(students[1])
