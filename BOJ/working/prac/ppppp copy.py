
h = 'long_and_mnemonic_identifier'

h = h.split('_')
for i in h:
    i = i.replace(i[0], i[0].upper())
    print(i[0])
print(h)