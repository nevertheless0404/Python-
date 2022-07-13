# 1부터 n까지의 합을 구하여 출력하는 코드를 1)while 문
# 2) for 문으로 각각 장성하시오. 
# sum() 함수 사용 금지

n = 10

# while 문
i = 1
result = 0
while i <= n:
    result += i
    i += 1
print(result)

# for 문
result = 0
for i in range(n+1):
    result += i
print(result)
