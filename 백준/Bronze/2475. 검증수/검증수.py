# 첫째 줄에 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어진다.

arr = input().split()
n1, n2, n3, n4, n5 = int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3]), int(arr[4])
sum_val = 0

# 검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지이다.
v1 = n1 ** 2
v2 = n2 ** 2
v3 = n3 ** 2
v4 = n4 ** 2
v5 = n5 ** 2

sum_val = (v1 + v2 + v3 + v4 + v5) % 10

print(sum_val)