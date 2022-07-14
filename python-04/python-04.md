# Python 

## 데이터구조

📌 **input().split()** : 문자열.split()

📌 **[1,2,3].append(4)** : 리스트.append(4)

 #### → 타입.메서드()

### 🖍 메서드(methods)

```python
# 리스트 매서드 활용
a = [10, 1, 100]
# 정렬(sort)
new_a = a.sort()
print(a, new_a)
# [1, 10, 100] None
# 리스트 메서드를 활용하면, 그 메서드를 정렬된 상태로 변경(원본 변경)
# return 되는 것은 None

# 리스트 sotrted 함수
b = [10, 1, 100]
# 정렬(sort)
new_b = sorted(b)
print(b, new_b)
# [10, 1, 100] [1, 10, 100]
# sorted 함수를 활용하면, 원본을 변경하지 않음
# return되는 것은 정렬된 리스트 

# 실제 활용 코드
a = [10, 1, 100]
a.sort()
# a를 정렬된 상태로 활용

b = [10, 1 100]
b = sorted(b)
# b를 정렬된 상태로 활용 
```

#### 문자열(string Type)

- .find(X)
  - x의 첫 번째 위치를 반환. 없으면 -1을 반환함

```python
'apple'.find('p')
# 1
'apple'.find('k')
# -1
```

- .index(x)
  - x의 첫 번째 위치를 반환. 없으면, 오류 발생

```python
'apple'.index('p')
# 1
'apple'.find('k')
# valueError : substring not found
```

**문자열 관련 검증 메소드**

```python
'abc'.isalpha()
# 알파벳 True
'Ab'.isupper()
# 대문자 False
'ab'.islower()
# 소문자 True
'Title Title!'.istitle()
# 앞이 대문자 True
```

📎 **문자열 변경**

- .replace(ole, new[,count])

```python
'coone'.replace('O','a')
# caane
'wooooowoo'.replace('O','!',2)
# w!!ooowoo
```

- ⭐️ .strip([chars])
  - 특정한 문자들을 지정
  - 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip)
  - 문자열을 지정하지 않으면 공백을 제거함

```python
'      와우!\n'.strip()
# '와우!'
'      와우!\n'.lstrip()
# '와우!\n'
'      와우!\n'.rstrip()
# '    와우!'
'안녕하세요?????'.rstrip(?)
#'안녕하세요'
```

- ⭐️ .Split(sep=None, maxsplit=-1)
  - 문자열을 특정한 단위로 나눠 리스트로 반환

```python
'a,b,c'.split('_')
# ['a,b,c']
'a,b,c'.split()
#['a', 'b', 'c']
```

- ⭐️ 'separator'.join([iterable])
  - 반복가능한 컨테이너 요소들을 separator(구분자)로 함쳐 문자열 반환
  - 문자열이 아닌 값이 있으면 TypeError 발생

```python
''.join(['3', '5'])
# 35
```

----

#### 리스트(list)

> 변경 가능한 값들의 나열된 자료형

> 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음

> 변경 가능하며(mutable), 반복 가능함(iterable)

> 항상 대괄호 형태로 정의하며, 요소는 콤마로 구분

- ⭐️ .append(x)
  - 리스트에 마지막에 항목을 추가함

```python
cafe = ['starbucks','tomntoms','hollys']
cafe.append('banapresso')
#['starbucks','tomntoms','hollys','banapresso']

cafe.extend(['카페베네','테스트'])
# ['starbucks','tomntoms','hollys','카페베네','테스트'] 순차적으로 하나씩 들어감 
```

- .extend(iterable)
  - 리스트에 iterable의 항목을 추가함

- .insert(i, x)
  - 리스트 인덱스 i에 항목 x를 삽입

- .remove(x)
  - 리스트에서 값이 x인 것 삭제

- ⭐️ .pop(i)
  - 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함
  - i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함

```python
numbers = ['hi',1,2,3]
#['hi',1,2,3]
pop_number = numbers.pop()
# 3 


numbers = ['hi',1,2,3]
# ['hi',1,2,3]
pop_number = numbers.pop(0)
# 'hi'
print(numbers)
# [1,2,3]
```

- .clear()
  - 모든 항목 삭제 

- .index(x)
  - x값을 찾아 해당 index값을 반환

- ⭐️ .count(x)
  - 원하는 값의 개수를 반환함

```python
numbers = [1,2,3,1,1]
numbers.count(1)
# 3
number.count(100)
# 0
```

- ⭐️ .sort()
  - 원본 리스트를 정렬함 None 반환
  - sorted 함수와 비교할 것

- .reverse()
  - 순서를 반대로 뒤집음(정렬하는 것이 아님)

----

#### 딕셔너리(Dictionary)

- .get(key[,default])
  - key를 통해 value를 가져옴
  - keyError가 발생하지 않으며, default 값을 성정할 수 있음

```python
my_dict = {'apple':'사과','banana':'바나나'}
my_dict['pineapple']
#---------------------------------------
#keyErrorr

my_dict = {'apple':'사과','banana':'바나나'}
print(my_dict.get('pineapple'))
# None
print(my_dict.get('apple'))
# 사과
print(my_dict.get('pineapple',0))
# 0
```

- .Pop(key[,default])
  - key가 딕셔너리에 있으면 제거하고 해당 값은 반환
  - 그렇지 않으면 default를 반환
  - default값이 없으면 keyError

```python
my_dict ={'apple':'사과','banana':'바나나'}
date = my_dict.pop('apple')
print(date, my_dict)
# 사과{'banana':'바나나'}
```

- .update([other])
  - 값을 제공하는 key, value로 덮어습니다.

