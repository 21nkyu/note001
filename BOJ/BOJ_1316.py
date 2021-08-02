#리스트 두개 만들고
#하나는sort해서 
#두개 리스트 비교 하는데 
# 리스트가 len(리스트) = 0
# cnt+1
# 그게 아니면 0

# n = int(input())

# for _ in range(n):
#     words = input()
#     set_words = list(set(words))
#     cnt = 0
    
#     for i in range(len(set_words)):
#         for j in range(len(words)):
#             print(set_words[i], words[j])
#             if set_words.index(set_words[i]) - words.index(words[j]) > 2:
#                 cnt += 0 
#             else:
#                 cnt += 1

             
    
#     print(cnt)

# n = int(input())

# for _ in range(n):
#     words = input()
#     odd_n  = []
#     even_n = []
#     cnt = 0
#     for idx in range(0, len(words), 2):
#         odd_n.append(words[idx])
#     for idx in range(1, len(words), 2):
#         even_n.append(words[idx])
#     print(odd_n)
#     print(even_n)




# n = int(input())
# group = 0
# for _ in range(n):
#     word = input()
#     error = 0
#     for i in range(len(word)-1):
#         if word[i] != word[i+1]:
#             print('back:', word[i], 'front:',word[i+1])
#             new_word = word[i+1:]
#             print('new_word:',new_word)
#             print('word[i]:', word[i], 'new_word.count(word[i]):', new_word.count(word[i]), 'new_word:', new_word)
#             print("====================if word in new_word")
#             if new_word.count(word[i]) > 0:
                
#                 error += 1
#                 print('error:', error)
#                 print("===========================")
#     print('error:', error)
#     if error == 0:
#         group += 1
# print(group)


# aabbcccb
# 1
# 12
# ab
# new_word = b
# 2
# 23 bb
# 3
# 34 bc
# new_word = bc
# 6
# 67 cb
# new_word = bcb  




n = int(input())
group = 0
for _ in range(n):
    word = input()
    error = 0
    for idx in range(len(word)-1):
        if word[idx] != word[idx+1]:
            new_word = word[idx+1 : ]
            if new_word.count(word[idx]) > 0:
                error += 1
    if error == 0:
        group += 1

print(group)

#find를 이해하면 빠른데 이해가 잘 안됨
N = int(input())
cnt = N
for _ in range(N):
    word = input()
    for i in range(len(word)-1):
        if word.find(word[i]) > word.find(word[i+1]):
            cnt -= 1
            break
print(cnt)