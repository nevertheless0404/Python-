# python

## OOP

### 객체 지향 프로그래밍

> 컴퓨터 프로그래밍의 패러다임 중 하나이다. 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 

> 객체(object)는 특정 타입(클래스)의 인스턴스(intstance)이다.

#### 객체

- 객체의 특징
  - 타입(type): 어떤 연산자와 조각이 가능한가?
  - 속성(attribute): 어떤 상태(데이터)를 가지는가?
  - 조작법(method): 어떤 행위(함수)를 할 수 있는가?

```python
'abc'.upper()
-------------------
tranform_uppercase('abc')
```

- 현실 세계를 프로그램 설계에 반영(추상화)

```python
class person:
	def__init__(self, name, gender):
    self.name = name
    self.gender = gender
    
  der greeting_message(self):
    return f'안녕하세요, {self.name}입니다.'

jimin = person('지민','남')
print(jimin.greeting_message())
# 안녕하세요, 지민입니다.

jieun = person('지은','여')
print(jieun.greeting_message())
# 안녕하세요, 지은입니다.
```

##### 📌 클래스 : str, person, ...

##### 📌 인스턴스 : '123', iu

##### 📌 객체 : 모든 것 

-----

### OOP기초

```python
# 사각형 - 클래스
class Rectangle:
  	def __init__(self, x, y):
      	self.x = x
        self.y = y

    # 각 사각형 - 인스턴스
    def area(self):
      	# 사각형의 행동/기능 - 메소드 (넓이 구하기, 높이 구하기)
      	return self.x * self.y

    def circumference(self):
      	return 2 * (self.x + self.y)

# 사각형의 정보 - 속성 (가로 길이, 세로 길이)
r1 = Rectangle(10, 30)
# 메소드 호출
r1.area()
r1.circumference()

r2 = Rectangle(300, 20)
r2.area()
r2.circumference()
```

- 기본 문법

```python
# 클래스 정의
class MyClass:
    pass
# 인스턴스 생성
my_instance = Myclass()
# 메서드 호출
my_instance.my_method()
# 속성
my_instance.my_attribute
```

- 클래스와 인스턴스
  - 클래스 : 객체들의 분류
  - 인스턴스 : 하나하나의 실체

- 속성
  - 특정 데이터 타입/클래서의 객체들이 가지게 될 상태/데이터를 의미

- 메소드
  - 특정 데이터 타입/클래서의 객체에 공통적으로 적용 가능한 행위(함수)

- 객체 비교하기 

  - ==
    - 동등한 (equal)
    - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 true
    - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 환인해 준 것은 아님

  - is
    - 동일한 (identical)
    - 두 변수가 동일한 객체를 가리키는 경우 true

----

### 추상화

> 현실 세계를 프로그램 설계에 반영(추상화)

```python
class Person:
  	def __init__(self, name, age, gender):
      	self.name = name
        self.age = age
        self.gender = gender

    def info(self):
      	return (self.name, self.age, self.gender)

hong = Person('홍길동', 100, 'M')
ko = Person('고길동', 40, 'M')

print(hong.info())
print(hong.name)
print(hong.age)
```

## **인스턴스 메소드**

> - 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
> - 클래스 내부에 정의되는 메소드의 기본
> - 호출 시, 첫번째 인자로 인스턴스 자기자신 (self)이 전달됨



- self
  - 인스턴스 자기자신
  - 호출 시 첫번째 인자로 `인스턴스 자신이 전달되게 설계`
  - 매개변수 이름으로 self를 `첫번째 인자` 로 정의
  - 파이썬에서 `암묵적인 규칙`



- 생성자(Constructor) 메소드
  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
  - 인스턴스 변수들의 초기값을 설정
    - 인스턴스 생성
    - `__init__` 메소드 자동 호출

```python
class Person:
  	# 생성자! 인스턴스가 생성될 때 어떠한 작업!
  	def __init__(self, name):
      	# 인스턴스의 이름을 name으로 설정
        self.name = name

# Person 클래스의 인스턴스인 iu, jimin 설정
iu = Person('아이유')
jimin = Person('지민')

print(iu.name)
print(jimin.name)
```



- 소멸자(Destructor) 메소드
  - 인스턴스 객체가 소멸되기 직전에 호출되는 메소드
  - `__del__`

```python
class Person:
    def __del__(self):
        print('인스턴스가 사라졌습니다')
```

