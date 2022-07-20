# 입력으로 1개의 정수 n이 주어진다.
# 정수 n의 약수를 오름차순으로 출력하는 프로그램

import sys
sys.stdin = open("/Users/yuyeong/Desktop/Python/python-07/간단한.txt","r")



n = int(input())
for i in range(1, n+1):
    if n%i == 0:
        print(i, end = " ")


