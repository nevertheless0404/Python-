# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# min() 함수 사용 금지


import numbers


numbers = [-10, -100, -30]
# float("-inf")
min_num = numbers[0]
# 1. 반복
for n in numbers:
    # print(n)
    if min_num > n:
        min_num = n
print(min_num)