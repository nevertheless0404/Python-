# n의 배수 번호인 양을 세기

import sys
sys.stdin = open("/Users/yuyeong/Desktop/Python/python-08/1288.txt","r")

# t = int(input())

# for i in range(1, t +1):
#     # 각 테스트 케이스마다 n을 문자열 형태로 입력받아 정수형으로 변환
#     # 변환한 값을 value로 할당
#     n = input()
#     value = int(n)
#     # 자리수의 번호를 셀 횟수
#     date = [0] * 10
#     while True:
#         # 각 자리수를 하나씩 확인하여 그 값을 인덱스로 하여 1씩 증가
#         for j in range(len(n)):
#             date[int(n[j])] += 1
        
#         # 요소들 중 0이 없을 경우 모든 숫자가 최소 한번씩 세어진 것이므로 멈준다.
#         if not date.count(0):
#             print('#%d %d' % (i, int(n)))
#             break

#         n = str(value + int(n))


# tip!!
# $s 문자열 출력
# %d 정수출력
# %f 실수 출력

T = int(input())
for test_case in range(1, T+1):
    # input 가져오기 
    N = int(input())
    N1 = N
    # set에 계속 추가 예정
    numbers = set()
    #  while 반복 => set 길이가 10이 될 때까지
    while True:
        # for 반복 : 숫자를 문자로
        for n in str(N):
           # numbers set추가 
            numbers.add(n)
        if len(numbers) < 10:
            break
       # print(n, numbers)
        N += N1
    print(f'#{test_case} {N}')
        
