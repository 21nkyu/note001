# https://www.acmicpc.net/problem/3613


# # j = [h[i].lower() for i in range(len(h)) if h[i].isupper()]
# j = []


h = input()

if '_' in h and h.islower() == True:
    for i in range(len(h)-1):
        if h[i] == '_':
            print(h[i+1].upper(), end='')
        else:
            print(h[i-1], end='')

elif '_' not in h and h.islower() == False:
    for i in range(len(h)):
        if h[i].isupper():
            print(h[i].lower(), end='')
        else:
            print(h[i], end='')

else:
    print("Error!")


#=======================================
# h = 'longAndShortButNo'
# h=input()
# for i in range(len(h)):
#     if h[i].isupper():
#         print(h[i].lower(), end='')
#     else:
#         print(h[i], end='')

# h='long_and_home'
# for i in range(len(h)):
#     if h[i] == '_':
#         print(h[i+1].upper(), end='')
#     else:
#         print(h[i], end='')