# 15964 (1.7,  https://www.acmicpc.net/problem/15964)

# 첫째 줄에 A, B가 주어진다. (1 ≤ A, B ≤ 100,000)
# 첫째 줄에 A＠B의 결과를 출력한다.

a, b = map(int, input().split())
print((a+b)*(a-b))

