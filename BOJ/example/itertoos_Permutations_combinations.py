from itertools import combinations, permutations

# 순열(permutation) 공식 : nPr = n!/(n-r)!
## 6P4 = 6 5 4 3 

a = [i for i in range(1,7)]
# print(permu_list)

# 6개중4개 조합 중복 허용 ex) 123 321 213
permute = list(permutations(a, 4)) # 360가지
print(f'permute : {permute}\n [6P4] : {len(permute)}가지')

#조합(combination) 공식 : nCr=nPr/r!

b = [i for i in range(1, 7)]

#6개중 4개조합 중복 허용하지 않음
combinate = list(combinations(a, 4))
print(f'combinate : {combinate}\n [6C4] : {len(combinate)}가지') #15가지