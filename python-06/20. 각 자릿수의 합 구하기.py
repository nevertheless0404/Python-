# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력

num = 123
# number가 0일 때 stop!
# => int는 0일 때 False

result = 0
while num:
    #몫은 다음 num이 됨
    #나머지는 더해나가면 된다
    result += num%10
    num //=10

    #2.
    #divmod(x,y)는 x를 y를 나누고, 
    #결과를 tuple로 변환
    # num, remainder = divmod(num, 10)
    # result += remainder

print(result)


