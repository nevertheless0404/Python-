# 2단부터 9단까지 반복아혀 구구단을 출력하세요.
# *문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

for dan in range(2, 10):
    print(f'{dan}단')
    for n in range(1,10):
        print(f'{dan} x {n} = {dan * n}')



# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

print("구구단 출력")
for x in range(2, 10):
    print("---[" + str(x) + "단]---")
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)
print("구구단 끝!")
        