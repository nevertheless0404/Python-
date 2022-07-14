# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u
# count()사용 금지

word = 'apple'
cnt = 0
# 지금은 인덱스가 필요없어서
# 그냥 char를 받을게요!
for i in word:
    #['a','e','i','o','u']
    # i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
    if i in 'aeiou':
        cnt += 1
print(cnt)
