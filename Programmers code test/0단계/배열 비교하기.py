arr1 = [49, 13]
arr2 = [70, 11, 2]

def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        return -1 if len(arr2) > len(arr1) else 1 #return 뒤에 if문을 만들수있다.
    else:
        sum1 = sum(arr1)
        sum2 = sum(arr2)
        if sum1 != sum2:
            return -1 if sum2 > sum1 else 1
        else:
            return 0
        
print(solution(arr1, arr2))