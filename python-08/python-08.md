# Python

✔️ **정확하게 어떻게 접근할것인지 생각해보기**

=> 이 사람이 왜 이 코드를 썼을까?

=> 왜 이 변수를 선언했지?

=> 이 반복문을 무슨 일을 하는 것이지?

=> 이 조건문은?

==> 각 코드의 정확한 의미를 파악

==> 내가 작성하려고 했던 반복문/조건문/변수와 도대체 무슨 차이 일까?

=======================================================

📌 이 값을 내가 어떤 타입으로 활용을 시작해야하는지가 중요!

📌 머릿속으로만 생각하지 말고 손 으로 코드 짜보기 천천히 되돌아보기!

------

## 파이썬 응용/심화

### list comprehension

- 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 것

- 1~3의 세제곱의 결과가 담긴 리스트 

```python
cubic_list = []
for number in range(1, 4):
	cubic_list.append(number**3)
print(cubic_list)
#----------------------------

[number**3 for number in range(1,4)]
# 특정한 원소(요소)로 구성된 리스트를 만들 때 
```

- 딕셔너리

```python
cubic_dict = {}
for number in range(1,4):
  cubic_dict[number] = number ** 3
print(cubic_dict)
#-------------------------------------

(number: number**3 for number in range(1,4))
```

### lambad

> 표현식을 계산한 결과값을 반환하는 함수, 이름 없는 함수여서 익명함수라고도 불림

- 특징
  - return문을 가질 수 없음
  - 간편 조건문 외 조건문이나 반복문을 가질 수 없음

- 장점
  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  - def를 사용할 수 없는 곳에서도 사용 가능 

### filter

> Filter(function, iterable)

> 순회 가능한 데이터 구조(iterable)의 모든 요소에 함수(function)적용하고,  그 결과가 True인 것들을 filter object로 변환

```python
# map(함수, 반복가능한 것)
# 반복 가능한 것들의 모든 요소에 함수를 적용시킨 결과를 
# map object로 반환한다.

# map(int, input().split())
# int형 변환함수를 input으로 받은 것을 쪼객 결과인 리스트에 각각 적용

numbers = [1,2,5,10,3,9,12]
result = []
for number in numbers:
  if number % 3 == 0:
    result.append(number*3)
print(reslut)

print(list(filter(lambda n : n%3==0, numbers)))

def is_3(n):
  return n % 3 ==0
print(list(filter(is_3, numbers)))

def is_3_1(n):
  if n % 3 ==0:
    return True
  else:
    return false
  
# 만약에 map으로 쓴다면? 함수를 정의!!

def mltiple_3(n):   # 정의!! 
  reture n * 3

print(list(map(mltiple_3,numbers)))
# 이 함수는 계속 사용되지 않고, map에서만 사용된다.
# 임시적인 함수를 만들고 싶다. => lambda

print(list(map(lambda n: n*3, numbers)))
```

Sum, len ... => 함수

Sum([1,2,3])  => 함수 호출

### 어노테이션

- 단순 메모로서 사용번에 대한 힌트를 제공
  - 동적 타입 언어인 파이썬을 정적 타입으로 확정시켜주는 것은 아님

```python
# 동적 타입 언어인 파이썬에서....
# 그냥 힌트.. 그냥 노트 

# 변수 어노테이션
a: int = 3
print(a)

# 함수 어노테이션 
def add(x: int, y: int) -> int:
  return x + y

print(add(7,4))
print(add('hi','hello'))

# 함수 어노테이션
def add2(x, y):
  return x + y
print(add2(7,4))
```

# 파이썬 버전별 업데이트

## 모듈 심화

- [파이썬 표준 라이브러리](https://docs.python.org/ko/3/library/index.html) : 파이썬에 기본적으로 설치된 모듈과 내장 함수

- 파이썬 패키지 관리자(pip) : PyPI에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

- 패키지 설치

  - 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치 가능
  - 이미 설치되어 있는 경우 알림을 띄우고 아무것도 하지 않음

- 패키지 활용 명령어

  ```python
  $ pip install SomePackage # SomePackage 설치
  $ pip install SomePackage==1.0.5 # SomePackage 버전 1.0.5 설치
  $ pip install 'SomePackage>=1.0.4'
  $ pip uninstall SomePackage # SomePackage 제거
  $ pip list # 패키지 목록 확인
  $ pip show SomePackage # 특정 패키지 정보 확인
  $ pip freeze > requirements.txt # 패키지 목록 내보내기
  $ pip install -r requirement.txt # 패키지 목록 일괄 설치
  $ pip install --upgrade pip # pip 버전 업그레이드
  ```

## 가상 환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치해야 함
- 여러 프로젝트를 하는 경우 버전이 서로 다를 수 있음
- 이러한 경우 가상 환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음

### venv

- 가상 환경을 만들고 관리하는데 사용되는 모듈

- 특정 폴더에 가상 환경을 만들고, 고유한 패키지 집합을 가질 수 있음

  - 특정 폴더에 가상 환경(패키지 집합 폴더)이 있고
  - bash같은 실행 환경에서 활성화 시키면
  - 해당 폴더에 있는 패키지를 관리 및 사용 가능

- 가상 환경을 생성하면 해당 폴더에 별도의 파이썬 패키지가 설치됨

  ```
  $ python -m venv <folder_name>
  ```

- 가상 환경 활성화 (`<venv>`는 가상 환경을 포함하는 폴더의 이름)

  | 플랫폼  | 셸              | 명령어                                |
  | ------- | --------------- | ------------------------------------- |
  | POSIX   | bash/zsh        | `$ source <venv> /bin/activate`       |
  |         | fish            | `$ source <venv> /bin/activate.fish`  |
  |         | csh/tcsh        | `$ source <venv> /bin/activate.csh`   |
  |         | PowerShell Core | `$ <venv> /bin/Activate.ps1`          |
  | Windows | cmd.exe         | `C:\> <venv>\Scripts\activate.bat`    |
  |         | PowerShell      | `PS C:\> <venv>\Scripts\Activate.ps1` |

- 가상 환경 비활성화

  `$ deactivate`