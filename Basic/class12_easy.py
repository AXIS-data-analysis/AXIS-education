# ==========================================
# [AXIS Basic반] 12회차 문제
# ==========================================
"""
문제 1. 다중 예외 처리 (try, except, finally)
다음은 문자열을 정수로 변환하는 코드입니다.
변환 중 발생할 수 있는 ValueError와 나머지 모든 에러를 처리하는 Exception 구문, 
그리고 마지막에 항상 실행되는 finally 구문을 작성하세요.

text = "일이삼"
"""
### 모범답안 ###
text = "일이삼"

# 1. try 블록 안에서 변수 text를 정수(int)로 변환하여 출력해 보세요.
try:
    number = int(text)
    print(number)
    
# 2. ValueError가 발생할 경우 "숫자로 변환할 수 없는 값입니다."를 출력하세요.
except ValueError:
    print("숫자로 변환할 수 없는 값입니다.")
    
# 3. 그 외 알 수 없는 모든 에러가 발생할 경우를 대비하여 Exception을 처리하고, 에러 원인을 함께 출력하세요.
except Exception as err:
    print(f"알 수 없는 에러가 발생했습니다: {err}")
    
# 4. finally 블록을 사용하여 정상 동작이든 에러든 상관없이 항상 "변환 시도 종료"가 출력되도록 하세요.
finally:
    print("변환 시도 종료")


"""
문제 2. 내장 모듈 (random) 활용하기
파이썬에서 기본으로 제공하는 random 모듈을 사용하여, 
오늘의 점심 메뉴를 무작위로 추천해 주는 코드를 작성하세요.

menus = ["김치찌개", "돈까스", "짜장면", "햄버거"]
"""
### 모범답안 ###
# 1. random 모듈 전체를 가져오거나, from ~ import 를 활용해 choice 함수만 가져오세요.
import random

menus = ["김치찌개", "돈까스", "짜장면", "햄버거"]

# 2. random.choice()를 사용하여 menus 리스트 중 하나를 무작위로 선택해 변수에 저장하세요.
selected_menu = random.choice(menus)

# 3. f-string을 사용하여 선택된 메뉴를 출력하세요.
#    * 출력 예시: 오늘의 추천 점심 메뉴는 돈까스입니다!
print(f"오늘의 추천 점심 메뉴는 {selected_menu}입니다!")


"""
문제 3. 패키지와 모듈 직접 만들고 불러오기
여러분이 직접 코드를 통해 'nadocoding'이라는 패키지(폴더)를 만들고, 
그 안에 'goodjob.py'라는 파이썬 파일(모듈)을 생성한 뒤 불러와 봅시다.
"""
### 모범답안 ###
import os

# [단계 1] 패키지와 모듈 생성하기 (파일 입출력 복습)
# 1. os.makedirs()를 사용해 "nadocoding"이라는 이름의 폴더를 만드세요.
os.makedirs("nadocoding", exist_ok=True)

# 2. with open()을 사용해 nadocoding 폴더 안에 "goodjob.py" 파일을 쓰기 모드("w")로 여세요.
with open("nadocoding/goodjob.py", "w", encoding="utf8") as f:
    # 3. 파일 안에 def say(): print("참 잘했어요!") 코드를 작성해 넣으세요.
    f.write("def say():\n    print(\"참 잘했어요!\")\n")

# [단계 2] 패키지와 모듈 불러오기
# 4. from ~ import 구문을 사용하여 nadocoding 패키지에서 goodjob 모듈을 가져오세요.
from nadocoding import goodjob

# 5. 불러온 모듈을 통해 모듈 안에 있는 say() 함수를 호출하세요.
goodjob.say()