# 1부터 n까지의 숫자에서 홀수는 더하고 짝수는 뺏을 때 최종 누락된 값


import sys
from unittest import result
sys.stdin=open("/Users/yuyeong/Desktop/Python/python-07/지그재그.txt","r")

T = int(input())
for i in range(1, T + 1):
    number = int(input())

    total = 1
    for c in range(2, number + 1):
        if c % 2: # 홀수
            total += c
        else: # 짝수
            total -= c

    print(f'#{i} {total}')
