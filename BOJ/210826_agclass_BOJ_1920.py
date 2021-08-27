# https://www.acmicpc.net/problem/1920
import sys

n = sys.stdin.readline()
nns =[i for i in map(int, input().split())]
nns = sorted(nns)
nns.sort()

print(nns)
m= sys.stdin.readline()
mms=[i for i in map(int, input().split())] #10만


for i in range(len(mms)): 
    if mms[i] in nns: #10만
        print(1)
    else:
        print(0)


# for i in range(len(mms)):
#     for j in range(len(nns)):
#         if mms[i] == nns[j]:
#             print(mms[i], nns[i])
#             print(1)
#         else:
#             print(0)

이진탐색

for tar_num in map(int, input().split()):#100000
    # O(log N) => 16.....
    전체길이값은 슬라이싱없이
    배열을 놓고 봤을때 
    지금 내가 보고있는 위치의 시작위치와 끝 위치를 알아야한다
    시작인덱스와 끝인덱스를 관리 해줘야 한다
    재귀의 경우도 파라미터와 리턴값으로 넘어가지 관리를 해줘야한다
    # 0 1 2 3 4 5 6
    # 0 1 2 3  0+3//2 == 1
    start_idx=0
    end_idx= n-1
    find_result = 0
    while s < e: #그래서 반복은
    # 반복을 고려해야한다 언제까지 반복해야하나 
    반으로 계속 나누다 보면 하나짜리 값이 나온다
    그경우에도 못찾았다 마지막 한칸에서 스타트나 미드 엔드가 모두 한칸짜리 값을 갖는다
    시작위치가 커버리는 것이 발생한다
    값이 없어서 어긋나는 경우
        mid_idx= start_idx + end_idx //2 
        # 비교를 해야한다
        # 같은지 확인 = 값을 찾았다
        # 같지 않은경우 어떤반쪽을 버릴지 확인
        # 세개 말고는 가짓수가 없다
        # if num_list[mid_idx] == target_num:
        #     pass
        # elif num_list[mid_idx] > tar_num:
        #     pass
        # elif


        if num_ > tar_nu:
            pass #엔드인덱스가 바뀌고 미드인덱스1 로
        elif n<tar_num:
            pass #뒤를 봐야한다 엔드인덱스는 그대로 스타트 인덱스만 미드+1로 온다
        else:
            find_reuslt =1# print(1)
            break

    print(find_result)


    재귀로 바꿔보기?아하..