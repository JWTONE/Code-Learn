'''
baejoon
'''
S = input()
C = list(S)
alphabets = range(1, 26)

for index, alphabet in enumerate(C):
    print(f'{index}{alphabet}')

print(alphabets)