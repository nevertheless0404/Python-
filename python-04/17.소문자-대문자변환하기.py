# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지


from unittest import result


word = 'banana'
result = ''

for i in word:
    result += chr(ord(i) -32)
print(result)

# number = ord(i)
# number = number -32
# resul += chr(number)