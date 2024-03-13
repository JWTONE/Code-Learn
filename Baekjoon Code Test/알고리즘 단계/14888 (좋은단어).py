N = int(input())
words = [input().strip() for _ in range(N)]

def count_words(N, words):
    count = 0
    
    for word in words:
        stack = []
        
        for string in word:
            if stack and stack [-1] == string:
                stack.pop()
            else:
                stack.append(string)
                
        if not stack:
            count += 1
            
    return count

result = count_words(N, words)
print(result)