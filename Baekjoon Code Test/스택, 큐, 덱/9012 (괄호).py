'''
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
'''

'''
3
((
))
())(()

'''

T = int(input())
for _ in range(T):
    input_string = input().strip()

    def check_string(string):
        open_string = 0
        close_string = 0
        
        for check in string:
            if check == '(':
                open_string += 1
            elif check == ')':
                close_string += 1
                
            if close_string > open_string:
                return False
            
        return open_string == close_string
    
    if check_string(input_string):
        print("YES")
    else:
        print("NO")