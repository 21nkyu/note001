#입력을 9개 받는다
#난쟁이는 7명
#7명의 모자에 적힌 수를 더하면 100이 된다
#모자에 적힌 수는 중복된 수는 없으며
#항상 답이 유일한 경우만 입력으로 주어진다

#문제를 푸는데 사용한 아이디어
#7개를 더해서 100이 나온다 = 9개를 더해서 100을 빼면 
#100이 되는 7개를 제외한 2개를 더해서 나오는 수와 같다 


nums = []                        # 입력받는 수를 넣을 리스트                  
sum_nums = 0                     # 입력받은 수를 더해주는 변수?  

for _ in range(9):               # 조건만큼 입력 받고 리스트 넣어주고 리스트의 원소의 값을 더해준다
    n = int(input())
    nums.append(n)
    sum_nums += n

t_l = []                         # t_l : 2개의 수를 넣을 리스트
t_n = sum_nums - 100             # t_n : 리스트의합 - 100 = 9개의 숫자 중에서 2개의 숫자를 조합해서 나와야 하는 값 
for i in range(len(nums)):       
    for j in range(len(nums)):  
        if nums[i] + nums[j] == t_n and nums[i] != nums[j] and nums[i] > nums[j]:
            t_l.append(nums[i])  #이중 for문을 돌면서 생기는 문제는  
            t_l.append(nums[j])  # 1) nums[i]와 nums[j]가 중복되는경우
for k in nums:                   # 2) (nums[i] nums[j]), (nums[j], nums[i]) 예를 들면 (15 25), (25 15)인 경우가 모두 리스트에 저장된다   
    if k not in t_l:             # 그래서 조건을 i + j = 40 and i != j and i > j
        print(k)                 # i > j는 좀 의아 할 수도 있는데 15 25, 25 15중 하나만 저장 되면 되기 때문에 리스트에 넣을때 중복을 없애려고 준 조건임

# 출력은 nums에 있는 원소k를 차례대로 돌면서
# t_l리스트에 k가 없다면 nums에 원소 k를 순서대로 출력하였음.





            