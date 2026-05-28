import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import glob
import os

# ==========================================
# 1. 데이터 로드 및 전처리
# ==========================================
print("Kaggle에서 광고 데이터를 다운로드하는 중입니다...")
path = kagglehub.dataset_download("ashydv/advertising-dataset")
csv_files = glob.glob(os.path.join(path, "*.csv"))
df = pd.read_csv(csv_files[0])

if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

# ==========================================
# 2. 4분할 데이터 시각화 대시보드 구성
# ==========================================
print("\n데이터 분석 대시보드 창이 뜹니다. 창을 닫아야 다음 회귀 분석 결과가 출력됩니다!")

# 2x2 사이즈의 도화지(Figure) 생성
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
fig.suptitle('Advertising ROI Analysis Dashboard', fontsize=20, fontweight='bold')

# "그래프 1 (좌측 상단): 전체 변수 간 상관관계 히트맵"
sns.heatmap(df.corr(), annot=True, cmap='Blues', fmt=".2f", linewidths=.5, ax=axes[0, 0])
axes[0, 0].set_title("1. Overall Correlation Heatmap")

# "그래프 2 (우측 상단): 매체별 판매량 상관계수 랭킹 (바 차트)"
# Sales와의 상관계수만 추출하여 내림차순 정렬
corr_with_sales = df.corr()['Sales'].drop('Sales').sort_values(ascending=False)
sns.barplot(x=corr_with_sales.index, y=corr_with_sales.values, ax=axes[0, 1], hue=corr_with_sales.index, legend=False, palette='viridis')
axes[0, 1].set_title("2. ROI Ranking by Medium (Correlation with Sales)")
axes[0, 1].set_ylabel("Correlation Coefficient")
axes[0, 1].set_xlabel("")

# "그래프 3 (좌측 하단): 1등 매체(TV)와 판매량 간의 회귀 분석 (스캐터 플롯 + 회귀선)"
sns.regplot(data=df, x='TV', y='Sales', ax=axes[1, 0], scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
axes[1, 0].set_title("3. Linear Regression: TV Budget vs Sales")

# "그래프 4 (우측 하단): 타겟 데이터(Sales)의 분포도"
sns.histplot(df['Sales'], kde=True, ax=axes[1, 1], color='purple')
axes[1, 1].set_title("4. Distribution of Target Data (Sales)")

# 그래프 간격 조절 및 출력
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show() # 여기서 창이 열립니다.

# ==========================================
# 3. 단순 선형 회귀 분석 수치 도출
# ==========================================
print("\n[머신러닝 선형 회귀 분석 수치 결과]")

X = df[['TV']]
y = df['Sales']

model = LinearRegression()
model.fit(X, y)

coef = model.coef_[0]
intercept = model.intercept_

print(f"도출된 회귀식: Sales = ({coef:.4f} * TV) + {intercept:.4f}")
print(f"데이터 해석: TV 광고비를 1단위 추가 투입할 때마다, 판매량은 평균적으로 '{coef:.4f}' 단위만큼 증가합니다.")