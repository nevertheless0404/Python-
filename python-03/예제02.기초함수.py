# 가로와 세로 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 
# rectangle를 정의하시오.
# 사각형 가로가 20, 세로가 30일 때의 결과를 출력하시오.

from unittest import result


def rectangle(a, b):
    area = a * b
    round = (a + b) * 2
    return area, round

result = rectangle(20, 30)
print(result)

