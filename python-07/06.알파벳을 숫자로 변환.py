# 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환


import sys
sys.stdin = open("/Users/yuyeong/Desktop/Python/python-07/알파벳.txt","r")

alpha = input()
for i in alpha:
    ans = ord(i)-64
    print(ans, end = " ")

# ord() 함수는 유니코드 문자에 대응되는 정수를 표현 
# 대문자 A는 65에 해당 
# for문의 i는 문자열 하나하나 읽는다.