def solution(my_string, is_prefix):     
    if is_prefix == my_string[:len(is_prefix)]:         
        return 1     
    else:         
        return 0
    

print(solution("banana", "ban"))   
print(solution("banana", "nan"))   
print(solution("banana", "abcd"))  
print(solution("banana", "bananan"))