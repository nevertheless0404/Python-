# Python

- 데이터를 기록  →  Key (Value) → 딕셔너리                        

```python
word = 'banana'
#print(word)
result ={}

#문자열을 반복하면서 알파벳 하나씩 char
for char in word:
  # 오류가 생기면 하나씩 ptint()넣어보기
  #만약에 기존에 키가 없으면 ,1로 초기화를하고 
  if char not in result:
    result[char] = 1
  #키가 있으면, 기존 값에 더하자!
  else:
    result[char] = result[char] + 1
    
#result[char] = result.get(char, 0) + 1
#result[char] 없으면 keyError
#result.get(char, 0) 없으면 None 
    
 prtin(result)
```



## 에러/예외 처리 (Error/ Exception Handing)

**branches** : 모든 조건이 원하는대로 동작하는지

**for loops** : 반복문에 진입하는지, 원하는 횟수만큼 실행되는지

**While loops** : for loops와 동일, 종료조건이 제대로 동작하는지

**function** : 

- Print 함수 활용
  - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나워서 생각
- 개발환경등에 제공하는 기능 활용
- python tutor 활용 (단순 파이썬 코드 경우)

- 뇌컴파일, 눈디버깅

### 문법 에러 (Syntax Error)

- SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문자가 발생한 위치 표현
- 줄에서 에러 감지된 가장 앞에 위치를 가리키는 캐럿(Caret)기호(^)를 표시

```python
if else
# file "<inpython-input-1>", lien 1 if else ^
```

### 예외(Exception)

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
- 실행중에 감지되는 에러들을 예외라고 부름
- 예외는 여러 타입으로 나타나고, 타입이 메시지의 일부로 출력된
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음

```	python
- ZeroDivisonError: 0으로 나누고자 할 때 
10/0
#---------
# ZeroDivisionError: division by Zero

- Name Error : namespace 상에 이름이 없는 경우
print(name_error)
#---------
# NameError: name 'name_error' is not defined

```

- TypeError : 타입 불일치

```python
1 + '1'
#--------
#TypeError: unsupported operand tpye(s) for +: 'int' and 'str'

round('3.5')
#--------
#TypeError: type str dosen't define_round_method
```

- TypeError - arguments 부족

```python
divmod()
#---------
#TypeError: divmod expected 2 arguments, got 0

import random 
random.sample()
#---------
#TypeError: sample() missing 2 reqired positional arguments: 'population' and 'k'
```

- TpyeError

```python
import random
random.sample(1, 2)
# TypeError: population must b a sequence or set. For dicts, use lis†(d).
```

- ValueErrod - 타입은 올바르나 값이 적절하지 않거나 없는 경우

```python
int('3.5')
#-------
# valueError: invalid literal for int() with base 10 : '3.5'
range(3).index(6)
#--------
# valueError: 6 is not in range
```

- indexError

```python
empty_list = []
empty_list[2]
# IndexError : list index out of range
```

-  keyError

```python
song = {'IU':'좋은날'}
song['BTS']
# KeyError : 'BTS'
```



### 예외 처리

- Try 문
  - 오류가 발생할 가능성이 있는 코드를 실행
  - 예외가 발생되지 않으면, except 없이 실행 종료

- except 문
  - 예외가 발생하면, except 문
  - 예외 상황을 처리하는 코드를 받아서 적절하게 조치를 취함

#### 예시

```python
num = input('숫자입력 : ')
print(int(num))
# 숫자입력:안녕
#ValueError: invalid literal for int() with '안녕'
```

- 파일을 열고 읽는 코드를 작성하는 경우
  - 파일 열기 시도
    - 파일이 없는 경우 =>'해당 파일이 없습니다.' 출력(except)
    - 파일 있는 경우 => 파일 내용을 출력(else)

- 해당 파일 읽기 작업 종료 메시지 출력(finally)

```python
# 파일이 없는 경우
try:
  f = open('noodfile.txt')
except FileNotFoundError:
  print('해당 파일이 없습니다.')
else:
  print('파일을 읽기 시작합니다.')
  print(f.read())
  print('파일을 모두 읽었습니다.')
  f.close()
finally:
  print('파일 읽기를 종료합니다.')
  

# 파일이 있는 경우
try:
  f = open('file.txt')
except FileNotFoundError:
  print('해당 파일이 없습니다.')
else:
  print('파일을 읽기 시작합니다.')
  print(f.read())
  print('파일을 모두 읽었습니다.')
  f.close()
finally:
  print('파일 읽기를 종료합니다.')
```

