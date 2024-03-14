'''
baejoon
'''
word = input()

for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) in word:
        print(word.index(chr(letter)), end=" ")
    else:
        print("-1", end=" ")
