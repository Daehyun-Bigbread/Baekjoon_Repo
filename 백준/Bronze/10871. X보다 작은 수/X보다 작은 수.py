# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    # X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다.
    if A[i] < X:
        print(A[i], end=" ")

# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다.
# X보다 작은 수는 적어도 하나 존재한다.