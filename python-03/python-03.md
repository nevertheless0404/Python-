# Python 

- for문은 변수에 들어있는 값을 한번씩 꺼낸다.

## 함수(function)

→  sum([1, 10, 100])

```python
numbers = [1, 10, 100]
result = 0
for number in numbers:
	result += number
```

#### Decomposition

> 기능을 분해, 재사용 가능

#### Abstraction 

> 복잡한 내용을 숨기고, 기능에 집중하여 사용할 수 있음. (블랙박스) 재사용성, 가독성, 생산성 

------

### 함수 기초 

**함수란?**

> 특정한 기능을 하는 코드의 조각(묶음)

> 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요시에만 호출하여 활용

### 사용자 함수 (Custom function )

- 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능

- 내장함수 활용(Built-in function)활용
- Pstdev 함수 (파이썬 표준 아리브러리 - statistics)

#### 📌 함수 기본 구조

- 선언과 호출 (define & call)

  - 함수의 선언은 def 키워드를 활용함
  - 들여쓰기를 통해 function body(실행될 코드 블록)
  - 함수는 parameter를 넘겨줄수 있음
  - 함수는 동작 후에 returnd을 통해 결과값을 전달함

  ```python
  # 정의
  # 1. def
  # 2. 함수 이름 : add
  # 3. Input : a, b
  def add(a,b):
    # 4. return : 값을 반환
    return a + b
  
  def minus(a, b):
    return a - b
  
  # 호출
  pirnt(add(5,10))
  print(minus(10,5))
  
  # 내장 함수 호출
  print(sum([1,2,3]))
  ```

- 입력 (Input)

  - Parameter vs argument

    - Parameter : 함수를 실행할 때, 내부에서 사용되는 식별자

    - Argument : 함수를 호출 할 때, 넣어준는 값

      - 호출 시 함수의 parameter를 통해 전달되는 값

      - ⭐️ **필수 Argument** : 반드시 전달되어야 하는 argument

      - ⭐️ **선택 Argument** : 값을 전달하지 않아도 되는 경우는 기본 값이 전달 

      - **Positional arguments** : 기본적으로 함수 호출 시 Arguments는 위치에 따라 함수 내에 전달됨

      - **Keyword arguments** : 직접 변수의 이름으로 특정 argument를 전달할 수 있음, keyword Arguments 다음에 positional Argument를 활용할 수 없음

        ```python
        def add(x, y):          add(x=2, y=5)
          return X + y          add(2, y=5)
        ```

      - **Default Argument Values** : 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함

        ```python
        def add(x, y=0)         add(2)
        		return x + y
        ```

      - 정해지지 않은 개수 arguments : 

        → 여러개의 positional Argument를 하나의 필수 parameter로 받아서 사용

        → 몇 개의 positional Argument를 받을지 모르는 함수를 정의할 때 유용

        ```python
        # 정해지지 않은 갯수의 인자
        def my_add(*numbers):
          # 내부적으로 numbers가 tuple
          # 여러개를 아구아구
          return numbers
        
        result = my_add(1,2,3)
        print(result, type(result)) #(1,2,3) <class 'tuple'>
        ```

        → 함수가 임의의 개수 Argument를 keyword Argument로 호출될 수 있도록 지정

        → Argument 들은 딕셔너리로 묶어 처리되며, Parameterdp ** 를 붙여 표현

        ```python
        def family(**kwargs):
          # 여러개인데 키워드로 내부에서 KWARGS 딕션어리로 활용
          for key, value in kwarge:
            print(ket, ":", value)
        ```

        

- 범위 (Scope)

  - 함수는 코드 내부에 local scope를 생성하며, 그 외 공간인 global scope

  - 객체 수명주기 

    - Bulit-in scope (print, sum, Len ...) : 파이썬이 실행된 이후부터 영원히 유지
    - global scope (a=3...) : 모둘이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    - Local scope (def...) : 함수가 호출될 때 생성되고, 함수가 종료될때까지 

  - 이름 검사 규칙 (name resolution)

    - 파이썬에서 사용되는 이름(식별자)들은 이름공강에 저장

    - 아래와 같은 순서로 이름을 찾아나감 LEGB rule라고 부름

      ![스크린샷 2022-07-13 오전 11.28.39](/Users/yuyeong/Desktop/Python/python-03/python-03.assets/스크린샷 2022-07-13 오전 11.28.39.png)

    - 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 안됨

      ```python
      print(sum)
      print(sum(range(2)))
      sum = 5
      print(sum)
      print(sum(range(2)))
      # 1
      # 5
      ```

      

- 결과값 (Output)

  - Return
    - 함수는 **반드시 값을 하나만** return한다.
      - 명시적인 return이 없는 경우에도 None을 반환한다.
    - 함수는 return과 동시에 실행이 종료된다.
  - Return vs print
    - returnd은 함수 안에서 값을 반환하기 위해서 사용되는 키워드
    - Print는 출력을 위해 사용되는 함수 

---

#### 함수 응용

- map(function, iterable)
  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과를 map object로 반환

```python
number = [1,2,3]
result = map(str, numbers)
print(result, type(result))

# <map object at 0x10e2ca100> <class 'map'>

list(reault) # 리스트 형변환을 통해 결과 직접 확인
# ['1', '2', '3']
```

![unknown](/Users/yuyeong/Desktop/Python/python-03/python-03.assets/unknown.png)