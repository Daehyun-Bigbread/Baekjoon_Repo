# 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데
# T 는 입력의 맨 첫 줄에 주어진다. 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며
# 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W).

T = int(input())

for i in range(T):
    h, w, n = map(int, input().split())  # H: 층수, W: 방수, N: 몇번째 손님

    floor = n % h # 객실의 층 (ex - 10 % 6 = 4층)
    room_line = (n // h)+1 #  손님이 배정될 호실 번호를 구함. 손님 번호를 층수로 나눈 몫에 1을 더해 방 번호를 계산

    if floor == 0: # 만약 손님의 수가 호텔 층수의 배수라면? 그래도 출력 + 1,
        floor = h
        room_line -= 1

    print(floor * 100 + room_line)



