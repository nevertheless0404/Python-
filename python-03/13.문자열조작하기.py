# 주어진 문자열 word가 주어질 때, 해당 단언를 역순으로 뒤집은 결과를 출력하시오.

fruit = "apple"
fruit_name = ''
# 1. for
for a in fruit:
    fruit_name = a + fruit_name
print(fruit_name)

# print(fruit[::-1])
# print(''.join(reversed(fruit))

word = 'apple'

for i in range(len(word)-1,-1-1):
    print(word[i],end='')


