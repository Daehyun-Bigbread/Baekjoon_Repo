# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A+B)