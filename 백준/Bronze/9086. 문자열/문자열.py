# 9086 (1.7,  https://www.acmicpc.net/problem/9086)

# 문자열을 입력으로 주면 문자열의
# 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

n = int(input())

for i in range(n):
    string = str(input())
    print(string[0], end='')
    print(string[-1])