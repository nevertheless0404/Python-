# 주어진 문자열 word가 주어질 때, 해당 단어 'a'를 모두 제거한 결과를 출력하시오.

from unittest import result


word = "apple"

for char in 'apple':
    if char != 'a':
        result = result + char
        # 반목문에서 아무것도 안하고 넘어가는?
        # continue
print(result)
    
