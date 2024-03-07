####################################################
#                   문자열 뽀개기                   #
####################################################
# 문자열 성격 알아 가기!

# 쌍따옴표와 홑따옴표
def print1():
    text1 = "\nhello, MJ's Club"    # \n 은 개행(줄바꿈)을 의미해요
    print(text1)
    
    text2 = '장범매니저님: 여러분 "퇴실 체크!"'
    print(text2)
    
    text3 = "팀스파르타\nlevel up!"
    print(text3)
#print1()


# 문자열 출력 포멧
def print2():
    who = "이수연매니저님: "
    number = 2024
    text = "말로 할 때 TIL 작성?^^"
    pi = 3.14159265
    print(f'\n{who}: {number}년 {text} {pi:.2f}')
    print("%s: %d년 %s %.2f" % (who, number, text, pi))  # %s 문자열 %d 정수 %f 실수
#print2()

# 문자열 합치기
def print3():
    text1 = "퇴근 "
    print(text1*20)
    
    text2 = "문제 다 풀때 까지는 불허"
    print(text1 + text2)
    
    '''
    형태(타입)가 다르면 합칠수 없어요. 형태 통일 필요
    number = 2024
    print(number+text1)
    '''
#print3()
    
# 특정 글자 검색/비교
def print4():
    text1 = "a"
    text2 = "z"
    text3 = "apple Zoo"
    if text1 in text3:
        print("\ntext1 in text3 = yes!")
    if text2 in text3:
        print("text2 in text3 = yes!")
#print4()


# 문자열에 사용할 수 있는 유용하고 자주쓰는 함수 몇가지 알아 가기!

# len() 함수: 문자열 길이 구하기!
def print4():
    text = "hello 여러분!"
    print(len(text))    #몇글자라고 나올까요?
    print(text[6])      #어떤 글자가 나올까요?
#print4()

# sorted() 함수: 문자열 아스키코드 값 기준으로 낮은 값 부터 정렬!
def print5():
    text = "apple@ BCDA!"
    print(sorted(text))
#print5()

# 변수.count('찾고싶은 문자or문자열') 함수 : 찾고싶은 문자or 문자열이 몇개 있는지!
def print6():
    text = "aaa bb c ddd hello 1234512345 여러분"
    print("\na 갯수: ", text.count('a'))
    print("dd 갯수: ", text.count("dd"))
    print("여 갯수: ", text.count("여"))
    print("3 갯수: ", text.count('3'))
#print6()
    
# 변수.index('찾고싶은 문자') 함수 : 찾고싶은 문자의 인덱스 번호!
def print7():
    text = "aaa bb c ddd hello 1234512345 여러분"
    print("\nc의 인덱스 번호: ", text.index('c'))  # 몇이 나올까요?
    print("bb의 인덱스 번호: ", text.index("bb")) # 몇이 나올까요?
#print7()

# 간단한 문자열 문제 몇개만 같이 풀어볼까요?

# 메인홈
# https://swexpertacademy.com/main/main.do
# 1989.초심자의 회문검사,  10804.문자열의 거울상 같이 풀어보기
# 1215.회문1, 2007패턴마디의 길이, 1979.어디에 단어가 들어갈 수 있을까, 1228.암호문1

####################################################
#                   재귀함수 뽀개기                 #
####################################################
# Return 하기 전에 함수는 아직 끝난것이 아니다! 살아있다! 명심!

# 만약 5 펙토리얼(!)을 계산한다고 했을 때 
def factorial(factorial_number):
    if factorial_number == 0:
        print("끝났다!")
        return 1
    else:
        print(f'factorial_number: {factorial_number}')
        result = factorial_number * factorial(factorial_number-1)
        print("result:", result)
        return result
    
print("\n최종 계산 값: ", factorial(5))


# 피보나치 수열 [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377...] 
# 1번째랑 2번째랑 더한게 3번째고, 2번째랑 3번째랑 더한게 4번째고, 3번째랑 4번째랑 더한게 5번째고...
# fibonacci_number 번째에 있는 피보나치 수를 구하여라

def fibonacci(fibonacci_number):
    if fibonacci_number == 0:
        print("0으로 끝!")
        return 0
    elif fibonacci_number == 1:
        print("1로 끝!")
        return 1
    else:
        print(f'factorial_number: {fibonacci_number}')
        result = fibonacci(fibonacci_number - 1) + fibonacci(fibonacci_number - 2)
        print("result:", result)
        return result
#print("\n최종 계산 값: ", fibonacci(5))

# 1217.거듭제곱

# for i in range(10) :
#     testcase = int(input())
#     N, M = map(int, input().split())

#     def power(N, M) :
#         if M == 0 :
#             return 1
#         else:
#             return N * power(N, M-1)

#     print(f'#{testcase} {power(N, M)}')