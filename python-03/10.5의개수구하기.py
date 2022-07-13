# 주어진 리스트의 요소 중에서 5개의 개수를 출력하시오

numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
n = 0
for five in numbers:
    if five == 5:
        n += 1
print(n)
