# 1부터 주어진 횟수까지 2극 곱한 값(들)을 출력
# 주어진 숫자는 30을 넘지 않는다.

import sys
sys.stdin = open("/Users/yuyeong/Desktop/Python/python-07/더블더블.txt","r")


T = int(input())
for i in range(0, T+1):
    print(2**i, end= " ")

# 출력이 1부터 되어야 하기 때문에 i=i*2 대신 i=2**1를 사용
