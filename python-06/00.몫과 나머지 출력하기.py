# import sys
# sys.stdin = open("/Users/yuyeong/Desktop/Python/python-06/input.txt","r")


T= int(input())
for i in range (1, T +1):
    a, b = map(int, input().split())
    print(f"#[{i} {a//b} {a%b}")
    
