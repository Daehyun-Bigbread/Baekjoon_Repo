# 9개의 서로 다른 자연수가 주어질 때
# 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

num_list = []

# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다
for i in range(9):
    num_list.append(int(input()))

# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
print(max(num_list))
print(num_list.index(max(num_list))+1)
