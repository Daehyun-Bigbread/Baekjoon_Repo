# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

n = int(input()) # 숫자 입력 리스트
numbers = list(map(int, input()))

print(sum(numbers))