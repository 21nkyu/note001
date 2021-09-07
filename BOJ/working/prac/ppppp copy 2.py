
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

space_list = [list(map(int, input().split())) for _ in range(M)]
print('space_list', space_list)

new_space_list = [[] for _ in range(M)]
dictionary = {}
for i in range(M):
    new_list = sorted(list(set(space_list[i])))
    print('new_list', new_list)
    for j in range(len(new_list)):
        dictionary[new_list[j]] = j
        print('dictionary', dictionary)
    for x in (space_list[i]):
        new_space_list[i].append(dictionary[x])
        print('new_space_list', new_space_list)

count = 0
for i in range(M - 1):
    for j in range(i + 1, M):
        if new_space_list[i] == new_space_list[j]:
            print('i', new_space_list[i], 'j', new_space_list[j])
            count += 1

print(count)