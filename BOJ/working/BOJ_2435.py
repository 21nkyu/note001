# https://www.acmicpc.net/problem/2435

h='long_and_home'
for i in range(len(h)):
    if h[i] == '_':
        print(h[i+1].upper(), end='')
    else:
        print(h[i], end='')