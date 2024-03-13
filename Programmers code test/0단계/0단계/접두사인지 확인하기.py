def solution(my_string, is_prefix):
    if my_string.startswith(is_prefix):
        return 1
    elif not my_string.startswith(is_prefix):
        return 0
    else:
        return is_prefix(my_string, is_prefix[:-1])
    

print(solution("banana", "ban"))   
print(solution("banana", "nan"))   
print(solution("banana", "abcd"))  
print(solution("banana", "banana"))