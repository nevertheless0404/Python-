# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정

# 문제 코드
# numbers = input().split()
# print(sum(numbers))
# sum 함수의 argumet는 int 


numbers = list(map(int, input().split()))
print(sum(numbers))
