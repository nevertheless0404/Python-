# 수도요금 프로그램

import sys
sys.stdin = open("/Users/yuyeong/Desktop/Python/python-07/수도요금.txt","r")

# R 이하 : Q
# R 초과 : Q + S*(W-R)

n = int(input())

for i in range(1, n + 1 ):
    P, Q, R, S, W= map(int, input().split())
    # print(P, Q, R, S, W)
    A = W * P
    # B = Q if 에 넣을 것!!!
    if R > W:
        B = Q
    else:
        B = Q + S*(W-R)
    print(f'#{i} {min(A,B)}')





