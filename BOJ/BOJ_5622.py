# alpha_front = 'abcdefghijklmnop'
# alpha_back  = 'qrstuvwxyz'

# words = input().split()

# apb = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
frnt_abp   = 'ABCDEFGHIJKLMNO'
fmddl_abp  = 'PQRS'
bmddl_abp  = 'TUV'
back_abp   = 'WXYZ'
words = input()

cnt = 0

for letter in words:
    if len(words)>=2 and len(words) <=15:  
        if letter in frnt_abp: 
            cnt += int(frnt_abp.index(letter)//3) + 3
            
        elif letter in fmddl_abp:
            cnt += 8
                    
        elif letter in bmddl_abp:
            cnt += 9
            
        else:
            cnt += 10

            

print(cnt)