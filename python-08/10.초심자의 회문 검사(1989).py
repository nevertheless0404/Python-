# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.


import sys
sys.stdin = open("/Users/yuyeong/Desktop/Python/python-08/1989.txt","r")

n = int(input())
for test_case in range(1, n +1):
    date = input()
    # 0부터 문자열 길이의 절반만큼 반복
    for i in range(len(date)//2):
    # 왼쪽 문자와 오른쪽 문자를 비교
        if date[i] != date[-1-i]:
            answer = 0
        else:
            answer = 1
    print("#{} {}".format(test_case, answer))



