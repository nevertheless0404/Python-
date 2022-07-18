# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드

number_list = [1,2,3,4,5,6,7,8,9,10]

total = 0
count = 0

for number in number_list:
    total += number
#count += 1 # 들여쓰기가 문제
    count += 1

# print(total // count) # 잘못된 부호
print(total / count)