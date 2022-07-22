# python

📌For: 순회 할때(문자열/리스트 등 ) + 횟수를 알 때 (range)

📌While: 조건에 도달할 때 까지 (while True + break )



### API(Application programming Interface)

: 응용프로그램 인터페이스 

- 컴퓨터나 컴퓨터 프로그램 사이의 연결
- 일종의 소프트웨어 인터페이스며 다른 종류의 소프트웨어에 서비스를 제공
- 사용하는 방법을 기술하는 문서나 표준 API 사양 명세(specification)

API를 사용하기 전에 확인해야 할 것:

어떻게 조작하는지!!!

Https:// 를 기반으로 보내주고 있었다.

- 요청하는 방식에 대한 이해
  - 인증 방식
  - URL 생성
    - 기본 주소
    - 원하는 기능에 대한 추가 경로
    - 요청 변수 (필수와 선택)

- 응답 결과에 대한 이해
  - 응답 결과 타입(JSON)
  - 응답 결과 구조 

```python
# pip install requests
import requests
# URL 로
order_currency = 'BTC'
payment_currency = 'KRW'
URL = F'https"//api.bithumb.com/public/ticker/{order_cuttency}_{payment_currency}
response = requests.get(URL)


# 응답 받은 값을 가져온다.
print(response, type(response)) #<Response [200]


#속성 예시
print(response.status_code)# 200
print(response.text, type(Response.text)) # 문자열

#메서드 예시
# .json() 텍스트에서 형식의 Json파일을 파이썬 데이터 타입으로 변경!
print(reponse.json(),type(response.json())) # <class 'dict'>

date = response.json()
# date는 딕셔너리 => key로 접근
print(date.get('date').get('closing_price'))
```

```python
import requests

order_currecy = 'ALL'
payment_currecy = 'KRW'
URL = f'주소입력'

# 리스폰이라는 변수에는, 리퀘스트로 가져온 주소에 접근, json 문서로 보여줘!
response = requests.get(URL).json()
# 코인스라는 변수에는, 리스폰 안에 'data'라는 키에 접근
coins = response.get('data')

# coins : 딕셔너리
# key : coin 이름
# value : 딕셔너리 (코인정보)
for coin is coins:
  # 문자열 오류가 발생해서 해당 문자열은 넘어갈 수 있게 조건문 설정🚨
  if doin != 'data':
    continue
  print(coin, coins.get(coin).get('opening_price'))


# 💡구조를 파악하고, 하나씩 파고들면 된다💡

# 🚨'str' 오류발생🚨
# - 딕셔너리로 구성된 문서 안에 맨 끝에 문자열이 있었음! 즉 이물질이 있었다!
```

#### 📚 참조

- 리퀘스트 공식 문서가 궁금하다면 [클릭](https://requests.readthedocs.io/en/latest/)



#### **랜덤 활용 예시**

```python
import random

print('======== 나이를 알려드립니다 ========')
name = input('이름을 입력해주세요: ')
print('================================')

# 이름마다 똑같은 숫자가 있으면 좋겠다라는 생각
# ord(지) 문자 => 숫자
# ord(영) 문자 => 숫자
# 합한 값을 가져가면 이름마다 같겠다
random.seed(sum(map(ord, name)))
# choice(a)는 하나 고르기
# sample(a, b)는 a에서 b개 고르기
print(f'{random.choice(range(10, 90))} 살 입니다.')
```