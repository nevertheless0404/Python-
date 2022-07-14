# 문자열 word가 주어질 때, 해당 문자열에서 a가 처음으로 
# 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1를 출력해주세요.
# find(), index() 메서드 사용 금지

# 원하는 숫자? 0,1,2,3,4,5
#얻는 방법은? ragne(len(word))

from unittest import result


word = 'banana'
for i in range(len(word)):
   # print(i, word[i])
   if word[i] == 'a':
    print(i)
    break
else:
    print(-1)



word = 'HappyHacking'
result = []
for i in range(len(word)):
    if word[i] == 'a':
        print(i,end='')
