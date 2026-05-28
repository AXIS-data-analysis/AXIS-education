# 먼저 필요한 라이브러리를 설치해야 합니다. (주피터 노트북 환경인 경우 아래 주석 해제 후 실행)
# !pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

# =========================================================
# [사전 준비] 실습용 가상 HTML 데이터 (문제 1, 2용)
# =========================================================
html_news = """
<div class="news-list">
    <div class="news-item">
        <h2 class="title"><a href="https://example.com/news/1">파이썬 데이터 분석, 왜 중요할까?</a></h2>
        <span class="date">2026-05-28</span>
    </div>
    <div class="news-item">
        <h2 class="title"><a href="https://example.com/news/2">웹 크롤링 시 주의해야 할 3가지</a></h2>
        <span class="date">2026-05-29</span>
    </div>
</div>
"""

html_reviews = """
<ul id="review-board">
    <li class="review">
        <span class="user">데이터장인</span>
        <span class="rating">★★★★★</span>
        <p class="content">정말 유익한 강의였습니다. 강추합니다!</p>
    </li>
    <li class="review">
        <span class="user">파이썬초보</span>
        <span class="rating">★★★★☆</span>
        <p class="content">조금 어려웠지만 복습하니 이해가 됩니다.</p>
    </li>
</ul>
"""


# ==========================================
# [AXIS Core반] 7회차 문제 (심화) - 모범답안
# ==========================================

"""
"문제 1. HTML 구조 파악 및 특정 요소 추출 (find)"
가상의 뉴스 포털 HTML 데이터(html_news)에서 첫 번째 뉴스 기사의 '제목(텍스트)'과 '링크 주소(href)'를 
추출하여 출력하는 코드를 작성하세요.
"""
### 모범답안 ###
print("--- [문제 1] 뉴스 기사 정보 추출 ---")
# 1. BeautifulSoup을 사용하여 html_news 문자열을 파싱(해석)할 준비를 합니다.
soup_news = BeautifulSoup(html_news, 'html.parser')

# 2. find()를 사용하여 첫 번째 <a> 태그를 찾습니다.
first_link_tag = soup_news.find('a')

# 3. 태그 내부의 글자(text)와 href 속성(attribute) 값을 각각 추출합니다.
news_title = first_link_tag.text
news_link = first_link_tag['href']

print(f"기사 제목: {news_title}")
print(f"기사 링크: {news_link}\n")


"""
"문제 2. 다중 요소 추출 및 텍스트 정제 (find_all)"
가상의 리뷰 게시판 HTML 데이터(html_reviews)에서 모든 리뷰를 수집하려고 합니다.
작성자, 별점, 리뷰 내용을 각각 추출하여 딕셔너리 형태로 묶은 뒤, 
이를 하나의 리스트에 담아 출력하는 코드를 작성하세요.
"""
### 모범답안 ###
print("--- [문제 2] 리뷰 데이터 수집 ---")
# 1. BeautifulSoup을 사용하여 html_reviews 문자열을 파싱합니다.
soup_reviews = BeautifulSoup(html_reviews, 'html.parser')

# 2. find_all()을 사용하여 class가 'review'인 모든 <li> 태그를 찾습니다.
reviews = soup_reviews.find_all('li', class_='review')

review_list = []

# 3. 반복문을 돌며 개별 리뷰 블록에서 세부 정보를 추출합니다.
for review in reviews:
    # strip()을 사용하여 텍스트 앞뒤의 불필요한 공백이나 줄바꿈을 제거합니다.
    user = review.find('span', class_='user').text.strip()
    rating = review.find('span', class_='rating').text.strip()
    content = review.find('p', class_='content').text.strip()
    
    # 딕셔너리 형태로 리스트에 추가합니다.
    review_list.append({"작성자": user, "별점": rating, "내용": content})

print(review_list, "\n")


"""
"문제 3. 실전 웹 크롤링 및 데이터프레임 저장 (requests + Pandas)"
크롤링 연습용 샌드박스 사이트(http://quotes.toscrape.com/)에 실제로 접속하여 데이터를 수집해 봅시다.
페이지에 있는 명언(text)과 작가(author)를 추출하여 Pandas 데이터프레임으로 만든 뒤,
'quotes_data.csv' 파일로 저장하는 코드를 작성하세요.
"""
### 모범답안 ###
print("--- [문제 3] 실전 명언 사이트 크롤링 ---")
# 1. requests.get()을 사용하여 타겟 URL의 웹페이지 정보를 요청합니다.
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# 2. 요청이 성공(상태 코드 200)했는지 확인합니다.
if response.status_code == 200:
    # 3. 응답받은 HTML(response.text)을 BeautifulSoup으로 파싱합니다.
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 4. 명언 정보가 담긴 모든 div 블록(class='quote')을 찾습니다.
    quote_blocks = soup.find_all('div', class_='quote')
    
    scraped_data = []
    
    for block in quote_blocks:
        # 명언 텍스트와 작가 이름을 추출합니다.
        text = block.find('span', class_='text').text
        author = block.find('small', class_='author').text
        scraped_data.append({"명언": text, "작가": author})
        
    # 5. 수집한 리스트를 Pandas 데이터프레임으로 변환합니다.
    df_quotes = pd.DataFrame(scraped_data)
    
    # 6. CSV 파일로 저장합니다. (한글 깨짐 방지를 위해 utf-8-sig 인코딩 권장)
    df_quotes.to_csv("quotes_data.csv", index=False, encoding="utf-8-sig")
    
    print("✅ 성공적으로 크롤링하여 'quotes_data.csv' 파일로 저장했습니다!")
    print(df_quotes.head(3))
else:
    print(f"웹페이지 요청에 실패했습니다. (상태 코드: {response.status_code})")