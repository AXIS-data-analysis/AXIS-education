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
# 2. 프로페셔널한 데이터 시각화 (EDA)
# ==========================================
print("\n시각화 창(그래프)이 뜹니다. 그래프 창을 닫아야 다음 통계 분석이 진행됩니다!")

# 그래프 사이즈 설정
plt.figure(figsize=(12, 5))

# 그래프 1: 프로모션별 매출 분포 (Boxplot)
plt.subplot(1, 2, 1)
sns.boxplot(x='Promotion', y='SalesInThousands', data=df, palette='Set2')
plt.title('Sales Distribution by Promotion')
plt.xlabel('Promotion Type')
plt.ylabel('Sales (in Thousands)')

# 그래프 2: 매장 규모(MarketSize)에 따른 프로모션 효과
plt.subplot(1, 2, 2)
sns.boxplot(x='MarketSize', y='SalesInThousands', hue='Promotion', data=df, palette='Set2')
plt.title('Sales by Market Size and Promotion')
plt.xlabel('Market Size')
plt.ylabel('Sales (in Thousands)')

plt.tight_layout()
plt.show() # 여기서 그래프 창이 열립니다. 창을 닫아야 아래 코드가 마저 실행됩니다.

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