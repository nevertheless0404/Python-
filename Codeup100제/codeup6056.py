# 2개의 정수값이 입력될 때,
# 그 불 값(True/False)이 서로 다를 때에만 True를 출력하는 프로그램

a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and (not b)) or ((not a) and b))