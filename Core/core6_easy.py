import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================================
# [사전 준비] 실습용 데이터셋(CSV) 불러오기 및 환경 세팅
# =========================================================
print("데이터를 불러옵니다...")

# 1. 인터넷 URL을 통해 레스토랑 결제 데이터(tips)를 즉시 불러옵니다.
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df_tips = pd.read_csv(url)

# 2. 시각화를 위한 한글 폰트 및 마이너스 기호 깨짐 방지 설정 (윈도우 기준)
# (맥 사용자의 경우 'Malgun Gothic' 대신 'AppleGothic'으로 변경해주세요)
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)

print("✅ 데이터 로드 및 환경 세팅 완료!\n")


# ==========================================
# [AXIS Core반] 6회차 문제 (심화) - 모범답안
# ==========================================

"""
"문제 1. 단일 변수 및 그룹별 패턴 분석 (Histplot & Boxplot)"
레스토랑의 전반적인 매출 형태와 요일별 패턴을 파악하려고 합니다.
1) 'total_bill'(총 결제금액)의 분포를 파악하기 위해 밀도 곡선(KDE)이 포함된 히스토그램을 그리세요.
2) 요일('day')별로 'total_bill'의 중앙값과 이상치를 한눈에 볼 수 있도록 박스플롯(Boxplot)을 그리세요.
"""
### 모범답안 ###

# 1-1. 총 결제금액 분포 확인 (히스토그램)
plt.figure(figsize=(8, 5))
# kde=True 옵션을 주면 데이터의 밀도를 나타내는 부드러운 곡선이 함께 그려집니다.
sns.histplot(data=df_tips, x="total_bill", kde=True, color="teal")
plt.title("총 결제금액(total_bill) 분포")
plt.show()

# 1-2. 요일별 결제금액 패턴 확인 (박스플롯)
plt.figure(figsize=(8, 5))
# x축을 요일(day)로, y축을 총 결제금액(total_bill)으로 설정합니다.
sns.boxplot(data=df_tips, x="day", y="total_bill", palette="Set2")
plt.title("요일별 총 결제금액 분포 및 이상치")
plt.show()


"""
"문제 2. 다변량 관계 분석 (Scatterplot & Hue)"
총 결제금액이 높을수록 팁(tip)도 많이 주는지, 그리고 식사 시간대(점심/저녁)에 따라 그 양상이 다른지 분석해봅시다.
x축은 'total_bill', y축은 'tip'으로 하는 산점도를 그리되, 
시간대('time')별로 색상을 다르게(hue) 설정하여 두 변수 간의 관계를 시각화하세요.
"""
### 모범답안 ###
plt.figure(figsize=(8, 6))

# scatterplot을 사용하며, hue 파라미터에 'time'을 주어 점심(Lunch)과 저녁(Dinner)을 구분합니다.
sns.scatterplot(
    data=df_tips, 
    x="total_bill", 
    y="tip", 
    hue="time", 
    alpha=0.8,
    palette="deep"
)
plt.title("총 결제금액과 팁의 상관관계 (시간대별)")
plt.show()


"""
"문제 3. 상관관계 분석 및 인사이트 리포트 도출 (Heatmap & Print)"
데이터셋 내의 모든 수치형 데이터(결제금액, 팁, 일행 수) 간의 상관계수를 계산하여 히트맵으로 시각화하고,
위의 1~3번 과정을 통해 도출해낸 '핵심 비즈니스 인사이트'를 문자열로 출력하는 코드를 작성하세요.
"""
### 모범답안 ###

# 3-1. 수치형 데이터만 추출하여 상관계수(corr) 계산
# object나 category 타입이 섞여 있으면 에러가 날 수 있으므로 숫자형(number)만 선택합니다.
df_numeric = df_tips.select_dtypes(include=['number'])
corr_matrix = df_numeric.corr()

# 3-2. 히트맵 시각화
plt.figure(figsize=(6, 5))
sns.heatmap(
    corr_matrix, 
    annot=True, 
    fmt=".2f", 
    cmap="Oranges", 
    vmin=-1, 
    vmax=1
)
plt.title("수치형 변수 간 상관관계 히트맵")
plt.show()

# 3-3. 분석 리포트 출력
print("=" * 50)
print("[데이터 분석 인사이트 리포트]")
print("=" * 50)
print("1. [매출 분포]: 대부분의 고객 결제금액은 10~20달러 사이에 집중되어 있습니다.")
print("2. [요일별 패턴]: 주말(Sat, Sun)이 평일보다 평균 결제금액이 높고 큰 손(이상치) 고객이 많습니다.")
print("3. [상관관계]: 총 결제금액(total_bill)과 팁(tip)은 양의 상관관계를 가집니다(상관계수 0.68).")
print("4. [시간대 특성]: 점심보다는 저녁(Dinner)에 결제 건수가 압도적으로 많으며, 고액 결제도 주로 저녁에 발생합니다.")
print("=" * 50)