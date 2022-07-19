# 10개의 수를 입력 받아, 평균값을 출력

# import sys
# sys.stdin = open("/Users/yuyeong/Desktop/Python/python-06/input3.txt","r")



n = int(input())
for i in range(1, n + 1):
    sum = 0
    numbers = list(map(int, input().split()))
    for k in numbers:
        sum += k
print("#{} {}".format(i, round(sum/len(numbers))))
