# import sys

# sys.stdin = open("/Users/yuyeong/Desktop/Python/python-06/input4.txt","r")




n = int(input())
for i in range(1, n +1):
    a, b = map(int, input().split())
    if a > b:
        print(f"#{i} >")
    elif a < b:
        print(f"#{i} < ")
    elif a == b:
        print(f"#{i} =")