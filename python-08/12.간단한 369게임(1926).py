# 입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를

# 게임 규칙에 맞게 출력하는 프로그램을 작성하라.

# 박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.

# 여기서 주의해야 할 것은 박수 한 번 칠 때는 - 이며, 박수를 두 번 칠 때는 - - 가 아닌 -- 이다.


import sys
sys.stain = open("/Users/yuyeong/Desktop/Python/python-08/1926.txt","r")

N = int(input()) # 1부터 출력할 숫자의 범위
for num in range(1, N +1 ):
    temp = num # 현재 숫자에서 (3,6,9)의 객수를 구하기 위한 변수 
    count = 0 # 현재 숫자에서 (3,6,9)의 객수
    while temp > 0: # 현재 수에서 검사할 숫자가 남아있다면
        if temp % 10 in [3, 6, 9]: # 가장 오른쪽 자리 수가 (3,6,9)안에 있다면
            count += 1 # 갯수 증가
        temp //= 10 # 현재 수 / 10

    if count > 0: # (3,6,9) 개수가 1개 이상이면
        print("-" * count, end=' ')
    else:
        print(num, end =' ') # 해당 수 출력
