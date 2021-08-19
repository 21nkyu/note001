# https://www.acmicpc.net/problem/1913

N=int(input())
# hold=10
# cnt = 1
# row = []
# for i in range(1, N+1):
#     row.append(i)
# for _ in range(N):
#     print(row, end='\n')
#     cnt+=1
#     hold *= cnt
array=[]

for i in range(1, N+1):
    for j in range(1, N+1):
        # print(i, j)
        array.append((i, j))
# print(array)



start_n = 0
end_n = len(array)
div_n = N
for k in range(start_n, len(array)+div_n, div_n):
    print_out = array[start_n:start_n+div_n]
    if print_out != []:
        print(print_out)
        start_n += div_n


# idx_array = []
# for idx, path in zip(range(1, 10), array):
#     print(idx, path)
#     idx_array.append((idx, path))


# start_n = 0
# end_n = len(idx_array)
# div_n = N
# for k in range(start_n, len(array)+div_n, div_n):
#     print_out = idx_array[start_n:start_n+div_n]
#     if print_out != []:
#         print(print_out)
#         start_n += div_n
# print(f'{idx_array[8]},{idx_array[7]}')


#     print(array)
# for l in range(0,N):
#     print(snail_path[l], end='\n')

