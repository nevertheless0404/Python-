# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

from unittest import result


word = 'banana'
dic = {}

for chr in word:
    # dic[chr] = dic.get(chr, 0) + 1
    if chr in dic:
        dic[chr] += 1
    else:
        dic[chr] = 1
print(dic)

# for chr in word:
# 딕셔너리에 키가 없으면?
# if not chr in dic:
# 키랑 값을 1으로 초기화 한다.
# dic[chr] = 1
# 딕셔너리에 키가 있으면?
# else:
# dic += 1


# 출력부분
for key in dic:
    print(key, dic[key])
