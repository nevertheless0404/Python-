# 아래 코드는 1부터 N까지의 숫자에 2극 롭해서 변수에 저장하는 코드

# AttributeError: 'tuple' object has no attribute 'append'

N = 10
# answer =() # append 함수는 list의 함수
answer = []
for number in range(1, N + 1):
# for number in range(N + 1): # 범위설정이 잘 못 됨
    answer.append(number * 2)

print(answer)
