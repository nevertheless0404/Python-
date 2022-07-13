# Python

### 제어문

> 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행

> 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함

> 제어문 순서도(flow chart)로 표현이 가능

------

### 조건문

> 조건문은 참/거짓을 판단할 수 있 조건식

- expresstion에는 참/거짓에 대한 조건식
  - 조건이 참인 경우 이휴 들여쓰기 되어있는 코드 블럭 실행
  - 이외의 경우 elese 이후 들여쓰기 되었는 코드 블럭을 실행
    - else는 선택적으로 활용 가능

```	python
if <expression>:
  # Run this Code block
else:
  # Run this Code block
```

- 아래의 순서도를 코드로 나타내세요

  <img width="347" alt="스크린샷 2022-07-12 오전 9 21 26" src="https://user-images.githubusercontent.com/108647801/178440639-4ab5b31c-8fe7-4873-b60a-17c79da8e3b5.png">

```python
a = 10
if a > =0:
  print('양수')
else:
  print('음수')
print(a)
```

- 홀수인지 확인하는 코드

> a%2==1

- 복수의 조건식을 활용할 경우 elif를 활용하여 표현함

```python
dust = int(input())

# dust가 150보다 크면, 매우 나쁨
if dust > 150:
    print('매우 나쁨')
# 80보다 크면, 나쁨
elif dust > 80:
    print('나쁨')
# 30보다 크면, 보통
elif dust > 30:
    print('보통')
# 좋은
else:
    print('좋음')
```

### 조건 표현식

```python
value = num # 참일경우 if num >= 0 # expression else -num (거짓일 경우)
```

```python
num = -10

# 1. 양수면 그대로
if num >=0:
  value = num

# 2. 음수면 -붙여서
else:
  value = -num
print(num, value)

# 조건 표현식 코드
value = num if num >= 0 else - num
```

```python
예시

num = 2
if num % 2:
  result = '홀'
else:
  result = '짝'
print(result)


→ num = 2
result = '홀' if num % 2 else '짝'
print(result)
```

-----

### 반복문

#### 반복문의 종류

- While 

  > while 문은 조건식이 참인 경우 반복적으로 코드를 실행

  - 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행

  - 코드 블록이 실행되고, 다시 조건식을 검사하여 반복적으로 실행

  - while문은 무한 루프를 하지 않도록 종료조건이 반드시 필요

```python
while <expression>:
  # code block
```

```python
a = 0
while a < 5:
  print(a)
  a += 1 #a = a+1
print('끝')
```

##### for 문

- for은 시퀀스(string, tuple, list, range) 포함한 순회가능한 객체(iterable)요소를 모두 순회함

  > 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음

```python
for fruit in ['apple','mango','banana'] #통 하나씩 꺼내서 확인 
	print(fruit)
print('끝')
```

- for 문 일반 형식

  > 🔻Iterable

  - 순회할 수 있는 자료형(str, list, dict 등)

  - 순회형 함수(range, enumerate)

- 문자열 순회
  - 사용자가 입력한 문자를 한 글자씩 세로로 출력하시오

```python
chars = input()
# hi
(한 글자씩 출력)
for char in chars:
  print(char)
  
for idx in range(len(chars)):
  print(chars[idx])
# h
# i
```

- Enumerate 순회
  - Enumerate()
    - 인덱스와 객체를 쌍으로 담은 열거형(enumerate)객체 반환
    - (Index, value) 형태의 tuple로 구성된 열거 객체를 반환

```python
members = ['민수','영희','철수']

for i in range(len(memvers)):
  print(f'{i} {memvers[i]}')
  
for i, member in enumerate(members):
  print(i, member)
```

- 딕셔너리 순회
  - 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

```python
grages = {'john':80, 'eric':90}
for name in grades:
  print(name)
 # john 
 # eric

grages = {'john':80, 'eric':90}
for name in grades:
  print(name, grades[name])
# john 80
# eric 90
```

-----

#### 반복문 제어

- break 
  - 반복문을 종료 
-  continue 
  - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행 

- for-else 끝까지 반복문을 실행한 이후에 else문 실행
  - 끝까지 반복문을 실행한 이후에 else문 실행
    - break를 통해 중간에 종료되는 경우 else 문을 실행되지 않음

```python
# break문을 만나면 반복문을 종료됨
n = 0
while true:
  if n == 3:
    break
   print(n)
  n += 1 #0 1 2
  
# continue 이루의 코드 블록은 수행하지 않고, 다음 반복을 수행
# continue를 만나면, 이후 코드인 print(i)가 실행되지 않고 바로 다음 반복을 시행
for i in range(6):
  if i % 2 == 0:
    	coutinue
    print(i) # 1 3 5

# for-else
for char in 'apple':
  if char == 'b':
    print('b!')
    break
else:
  print('b가 없습니다.') # b가 없습니다.
   


