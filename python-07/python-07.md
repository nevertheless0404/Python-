# python

## 객체지향 프로그래밍

- Instance_method

```python
# 클래스 정의
class person:
  pass

# 인스턴스 생성
p1 = person()
# 인스턴스 속성
p1.name = '홍길동'

print(p1.name)
# 홍길동
```

```python
class person:
  type = '사람'
  
  # 인스턴스 메서드
  # 인스턴스가 활용할 메서드 
  def greeting(self):
    print("안녕하세요!!:)")
    
iu = person()
iu.greeting()
# 안녕하세요!!:)

# 클래스 변수(속성)
print(person.type)
# 안녕하세요!!:)
# 사람
```

- self

```python
class person:
  
  # 사람이라면 이름을 가지고 있다.
  # 인스턴스를 만들 떄는 이름 정보를 받아서 하고 싶다.
  # 생성자 메서드
  def__init__(self, name):
    # 개별 인스턴스에 각각 name 속성을 지정
    self.name = name
  
  # self: 호출하느 인스턴스를 파이썬 내부적으로 전달해줌 
  # jimin.greeting() 이렇게 호출되면
  # 이런 느낌으로 person.greeting(jimin)
  def greeting(self):
    #print('안녕하세요, 지민입니다.') # 개별 인스턴스의 속성으로 쓰고 싶다.
    print(f'안녕하세요,{self.name}입니다.')

# 인스턴스 만들때
jimin = person('지민')
jimin.greeting()
# print(jimin.name)
# 지민 

hope = person('호석')
hope.greeting()
```

- Why_oop

```python
class Yasuo:
  
  def__init__(self):
    self.haelth = 100
    self.energy = 0
    
    
yasuo1 = Yasuo()
yasuo2 = Yasuo()
yasuo1.haelth = yasuo1.health - 20

print(yasuo1.health, yasuo2.health)
# 80 100
```

- random

```python
import random


# for i in range(5):
#    number = range(1, 46)
#    result = random.sample(number,6)
#    result.sort()
#    print(result)


# n을 넣으면
# 그 횟수만큼
def generate_lotto(n):
  result = []
	for i in range(5):
		number = range(1, 46)
    pick = random.sample(number, 6)
		pick.sort()
		result.append(pick)
  return result

def check(buy_numbers, result_numbers):
  return 0

# print(generate_lotto(5))

# 6개 숫자가 랜덤으로 나온다.

#------------------------
import lotto_function 

# 이 코드의 결과
# 로또 번호들의 리스트
buy_number = lotto_function.generate_lotto(5)

lotto_function.check(buy_number, [1,2,3,4,5,6])\
```

```python
import radom 

class Lotto:
  def generate_lotto(self):
    self.numbers = sorted(random.sample(range(1, 46),6))
    
    def get_money(self, real_numbers):
      if self.numbers == real_numbers:
        return 1000000000000000
      else:
        return 0
      
      
lotto = Lotto()
lotto.generate_lotto()
print(lotto.numbers)
print(lotto.get_money([1,2,3,4,5,6]))
#----------------------------------------

import lotto_class

lotto = Lotto() # 인스턴스
lotto.generate_lotto() #생성
print(lotto.numbers) #숫자
print(lotto.get_money([1,2,3,4,5,6])) #확인

# lotto 인스턴스로 속성 볼 수 있고(numbers)내가 생성도하고, 
# 확인(get_money)도 가능 
```

-----

### 클래스

#### 클래스 속성

- 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성
- 클래서 선언 내부에서 정의
- `classname`.`name`으로 접근 및 할당

#### 인스턴스와 클래스 간의 이름 공간

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스로 생성 

#### 클래스 메소드

- 클래스가 사용할 메소드
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫번째 인자로 클래스(cls)가 정의됨

#### 스태틱 메소드

- 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드

- 속성을 다루지 않고 단지 기능(행동)만을 메소드를 정의할 때, 사용

- @staticmthod 데코레이터를 사용하여 정의

- 호출시, 어떠한 인자도 전달되지 않음(클래스 정보에 접근/수정 불가)

  

![스크린샷 2022-07-20 오전 11.32.11](/Users/yuyeong/Desktop/Python/python-07/python-007.assets/스크린샷 2022-07-20 오전 11.32.11-8285304.png)

#### 📌 메소드 정리

- 인스턴스 메소드 : 호출한 인스턴스를 의미하는 self 매개 변수를 통해 인스턴스를 조작
- 클래스 메소드 : 클래스를 의미하는 cls 매개 변수를 통해 클래스를 조작
- 스태틱 메소드 
  - 인스턴스나 클래스를 의미라는 매개변수를 사용하지 않음
  - 일반 함수처럼 동작하지만 클래스의 이름공간에 귀속 됨

-----

### 객체지향의 핵심 4가지

#### 📌 추상화

#### 📌 상속

#### 📌 다양성

#### 📌 캡슐화

![이름 없는 노트북 (1)-1](/Users/yuyeong/Desktop/Python/python-07/python-007.assets/이름 없는 노트북 (1)-1.jpg)

---

#### 상속

> 클래스 간의 부모-자식 관계

- 상속 관련 함수와 메서드
  - In instance(object, classinfo)
  - issubclass
  - Super()
    - 자식클래스에서 부모클래스를 사용하고 싶은 경우에 사용된다.

- 정리
  - 파이썬의 모든 클래스는 object로부터 상속된다.
  - 부모 클래스의 모든 요소가 상속된다.
  - `**super()**`를 통해 부모 클래서의 요소를 호출할 수 있다.
  - 메소드 오버라이딩을 통해 자식 클래스에서 정의가 가능하다.

- 다중 상속
  - 두개 이상의 클래스를 상속받는 경우
  - 상속받은 모든 클래스의 요소

----

#### 다양성(Polymorphism)

- 여러 모양을 뜻한다.
- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미한다.
