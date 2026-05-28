import kagglehub
import pandas as pd
import scipy.stats as stats
import os
import glob
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# ==========================================
# 1. 데이터 로드 및 전처리
# ==========================================
print("데이터셋을 준비하는 중입니다...")
path = kagglehub.dataset_download("chebotinaa/fast-food-marketing-campaign-ab-test")
csv_files = glob.glob(os.path.join(path, "*.csv"))
csv_file_path = csv_files[0] 
df = pd.read_csv(csv_file_path)

print("\n[데이터 미리보기]")
print(df.head())

# ==========================================
# 2. 4분할 대시보드 데이터 시각화 (EDA)
# ==========================================
print("\n시각화 창(대시보드)이 뜹니다. 그래프 창을 닫아야 다음 통계 분석이 진행됩니다!")

# 2x2 사이즈의 도화지 생성 (전체 제목을 위한 여백 포함)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
fig.suptitle('A/B Test Campaign Analysis Dashboard', fontsize=20, fontweight='bold')

# "그래프 1 (좌측 상단): 프로모션별 평균 매출 (Bar Plot)"
# 평균값과 95% 신뢰구간(오차막대)을 보여주어 ANOVA 분석과 직접적으로 연결됩니다.
sns.barplot(x='Promotion', y='SalesInThousands', data=df, ax=axes[0, 0], palette='viridis', errorbar=('ci', 95))
axes[0, 0].set_title("1. Average Sales by Promotion (with 95% CI)")
axes[0, 0].set_xlabel("Promotion Type")
axes[0, 0].set_ylabel("Average Sales (in Thousands)")

# "그래프 2 (우측 상단): 프로모션별 매출 분포 (Boxplot)"
# 기존에 작성하셨던 코드입니다. 이상치(Outlier)와 중앙값을 한눈에 봅니다.
sns.boxplot(x='Promotion', y='SalesInThousands', data=df, ax=axes[0, 1], palette='Set2')
axes[0, 1].set_title("2. Sales Distribution by Promotion")
axes[0, 1].set_xlabel("Promotion Type")
axes[0, 1].set_ylabel("Sales (in Thousands)")

# "그래프 3 (좌측 하단): 매장 규모에 따른 프로모션 효과 (Boxplot)"
# 기존에 작성하셨던 코드입니다. 그룹별 세부 효과를 확인합니다.
sns.boxplot(x='MarketSize', y='SalesInThousands', hue='Promotion', data=df, ax=axes[1, 0], palette='Set2')
axes[1, 0].set_title("3. Sales by Market Size and Promotion")
axes[1, 0].set_xlabel("Market Size")
axes[1, 0].set_ylabel("Sales (in Thousands)")

# "그래프 4 (우측 하단): 프로모션별 매출 밀도 곡선 (KDE Plot)"
# 매출 데이터가 어느 금액대에 가장 많이 몰려있는지 산의 능선처럼 부드럽게 보여줍니다.
sns.kdeplot(data=df, x='SalesInThousands', hue='Promotion', fill=True, ax=axes[1, 1], palette='Set1', alpha=0.5)
axes[1, 1].set_title("4. Sales Density Distribution by Promotion")
axes[1, 1].set_xlabel("Sales (in Thousands)")
axes[1, 1].set_ylabel("Density")

# 제목 겹침 방지 및 여백 자동 조절 (이전 프로젝트의 노하우 적용!)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show() # 여기서 4분할 대시보드 창이 열립니다.

# ==========================================
# 3. 본격적인 통계 분석 (ANOVA 및 사후 검증)
# ==========================================
print("\n[통계 분석 결과]")

# 프로모션별 데이터 분리
promo_1 = df[df['Promotion'] == 1]['SalesInThousands']
promo_2 = df[df['Promotion'] == 2]['SalesInThousands']
promo_3 = df[df['Promotion'] == 3]['SalesInThousands']

# 일원배치 분산분석 (ANOVA)
f_stat, p_value = stats.f_oneway(promo_1, promo_2, promo_3)
print(f"1. ANOVA Test: F-statistic = {f_stat:.4f}, p-value = {p_value:.4e}")

if p_value < 0.05:
    print("-> p-value가 0.05보다 작으므로, 세 프로모션 간 매출 차이는 통계적으로 유의미합니다.")
    print("-> 어떤 프로모션 간에 차이가 있는지 사후 검증(Tukey HSD)을 진행합니다.\n")
    
    # 사후 검증 (Tukey HSD)
    tukey_result = pairwise_tukeyhsd(endog=df['SalesInThousands'], groups=df['Promotion'], alpha=0.05)
    print("2. Tukey HSD 사후 검증 결과:")
    print(tukey_result)
else:
    print("-> p-value가 0.05 이상이므로, 프로모션 간 매출 차이가 통계적으로 유의미하지 않습니다.")