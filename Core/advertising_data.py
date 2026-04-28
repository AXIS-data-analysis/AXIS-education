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

# 불필요한 인덱스 컬럼이 있다면 제거
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

print("\n[데이터 미리보기]")
print(df.head())

# ==========================================
# 2. 상관관계 시각화 (Heatmap)
# ==========================================
print("\n상관관계 히트맵 창이 뜹니다. 창을 닫아야 다음 회귀 분석이 진행됩니다!")
plt.figure(figsize=(8, 6))
# 데이터의 각 변수 간 상관계수를 계산하여 히트맵으로 시각화
sns.heatmap(df.corr(), annot=True, cmap='Blues', fmt=".2f", linewidths=.5)
plt.title("Correlation Heatmap: Media Budgets vs Sales")
plt.tight_layout()
plt.show() # 창이 열립니다. 닫아주세요.

# ==========================================
# 3. 단순 선형 회귀 분석 (가장 효율이 좋은 TV 광고비 기준)
# ==========================================
print("\n[머신러닝 선형 회귀 분석 결과]")

# 독립변수(X)와 종속변수(y) 설정
X = df[['TV']]   # TV 광고비
y = df['Sales']  # 판매량

# 선형 회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X, y)

# 모델의 기울기(Coefficient)와 절편(Intercept) 추출
coef = model.coef_[0]
intercept = model.intercept_

print(f"도출된 회귀식: Sales = ({coef:.4f} * TV) + {intercept:.4f}")
print(f"데이터 해석: TV 광고비를 1단위 추가 투입할 때마다, 판매량은 평균적으로 '{coef:.4f}' 단위만큼 증가합니다.")