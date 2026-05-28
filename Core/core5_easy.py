import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================================
# [사전 준비] 실습용 데이터셋(CSV) 자동 생성
# =========================================================
print("데이터셋 생성을 시작합니다...")

# 1. 월별 매출 데이터 (monthly_sales.csv)
df_monthly_gen = pd.DataFrame({
    "월": ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"],
    "매출액": [1500, 1600, 1800, 2200, 2500, 2800, 3100, 2900, 2600, 3200, 3800, 4200]
})
df_monthly_gen.to_csv("monthly_sales.csv", index=False, encoding="cp949")

# 2. 카테고리별 매출 데이터 (category_sales.csv)
df_category_gen = pd.DataFrame({
    "카테고리": ["전자기기", "의류", "식품", "생활용품", "뷰티", "스포츠"],
    "매출액": [8500, 4200, 5100, 2800, 3500, 1800]
})
df_category_gen.to_csv("category_sales.csv", index=False, encoding="cp949")

# 3. 고객 행동 데이터 (customer_data.csv)
np.random.seed(42)
n = 200
tiers = np.random.choice(["VIP", "Gold", "Silver"], n, p=[0.15, 0.35, 0.50])
visits = []
amounts = []

for tier in tiers:
    if tier == "VIP":
        visits.append(np.random.randint(15, 50))
        amounts.append(np.random.randint(100, 500) * 10000)
    elif tier == "Gold":
        visits.append(np.random.randint(5, 20))
        amounts.append(np.random.randint(30, 150) * 10000)
    else: # Silver
        visits.append(np.random.randint(1, 10))
        amounts.append(np.random.randint(5, 50) * 10000)

df_customer_gen = pd.DataFrame({
    "고객ID": [f"C{str(i).zfill(3)}" for i in range(1, n+1)],
    "나이": np.random.randint(20, 60, n),
    "고객등급": tiers,
    "방문횟수": visits,
    "장바구니담은횟수": [v * np.random.randint(2, 6) for v in visits],
    "총결제금액": amounts
})
df_customer_gen.to_csv("customer_data.csv", index=False, encoding="cp949")

print("✅ 실습용 데이터셋(CSV 파일 3개) 생성 완료!\n")


# =========================================================
# [AXIS Core반] 5회차 문제 (심화) - 모범답안
# =========================================================

# --- "데이터 불러오기" ---
# 위에서 생성한 CSV 파일들을 불러옵니다. (한글 인코딩 cp949 지정)
df_monthly = pd.read_csv("monthly_sales.csv", encoding="cp949")
df_category = pd.read_csv("category_sales.csv", encoding="cp949")
df_customer = pd.read_csv("customer_data.csv", encoding="cp949")

# --- "문제 1. 한글 폰트 설정 및 다중 시각화 (Lineplot & Barplot)" ---
# 한글 폰트 설정 (윈도우 환경 기준. 맥은 'AppleGothic' 사용)
plt.rc('font', family='Malgun Gothic')
# 마이너스 기호 깨짐 방지
plt.rc('axes', unicode_minus=False)

# 1-1. 선 그래프 (월별 매출 추이)
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_monthly, x="월", y="매출액", marker='o')
plt.title("월별 매출 추이")
plt.show()

# 1-2. 막대 그래프 (카테고리별 매출 비교)
plt.figure(figsize=(10, 5))
sns.barplot(data=df_category, x="카테고리", y="매출액", palette="Blues_d")
plt.title("카테고리별 매출 비교")
plt.show()


# --- "문제 2. 고객 행동 패턴 그룹화 시각화 (Scatterplot)" ---
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df_customer, 
    x="방문횟수", 
    y="총결제금액", 
    hue="고객등급", 
    alpha=0.7, 
    palette="Set2"
)
plt.title("고객 방문 횟수 대비 결제 금액")
plt.show()


# --- "문제 3. 다변량 데이터 상관관계 분석 (Heatmap)" ---
# 상관계수를 구하기 위해 수치형(int, float) 데이터만 따로 추출합니다.
df_numeric = df_customer.select_dtypes(include=['int32', 'int64', 'float32', 'float64'])
corr_matrix = df_numeric.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix, 
    annot=True,      # 수치 표기
    fmt=".2f",       # 소수점 둘째 자리까지
    cmap="coolwarm", # 색상 맵 설정
    vmin=-1, 
    vmax=1
)
plt.title("수치형 변수 간 상관관계 히트맵")
plt.show()