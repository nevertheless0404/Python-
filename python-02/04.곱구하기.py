# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.


# while 문
i = 1
count = 1
n = 5

while count <= n:
    i *= count
    count +=1
print(i)

# for 문
i = 1
n = 5

for count in range(n):
    i *= (count+1)
print(i)

