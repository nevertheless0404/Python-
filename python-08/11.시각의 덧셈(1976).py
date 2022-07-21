# 시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.

# (시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)


import sys
sys.stdin = open("/Users/yuyeong/Desktop/Python/python-08/1976.txt","r")


t = int(input())
for test_case in range(1, t + 1):
    h1, m1, h2, m2 = map(int,input().split())
    # 두 시각을 입력 받아 해당하는 두 값에 더한다.
    hr = h1 + h2
    mi = m1 + m2

    # 분 값이 59보다 클 경우 최종 시 값에 1을 증가, 분 값에 60을 감소
    if mi >= 60:
        hr += 1
        mi -= 60
    if hr > 12:
        hr -=12

    print('#{} {} {}'.format(test_case,hr,mi))