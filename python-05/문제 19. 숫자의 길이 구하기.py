# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지


num = 123
count = 0

while num > 0:
    num //= 10
    count += 1
# num이 0 이히가 아닌 경우 n을 10씩 나눌 때 마다 자릿수를 1씩 증가한다.
print(count)