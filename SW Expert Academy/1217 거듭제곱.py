for i in range(10) :
    testcase = int(input())
    N, M = map(int, input().split())

    def power(N, M) :
        if M == 0 :
            return 1
        else:
            return N * power(N, M-1)

    print(f'#{testcase} {power(N, M)}')