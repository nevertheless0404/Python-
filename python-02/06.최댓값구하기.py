# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지


import numbers


numbers = [-10, -100, -30]
# float("-inf")
max_num = numbers[0]
# 1. 반복
for n in numbers:
    # print(n)
    if max_num < n:
        max_num = n
print(max_num)
