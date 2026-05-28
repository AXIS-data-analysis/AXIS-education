# ==========================================
# [AXIS Core반] 4회차 문제 (실전 공공데이터)
# ==========================================
"""
\"문제 1. 결제 수단별 다중 통계 집계 (groupby와 agg)\"
뉴욕시 택시 운행 공공데이터를 인터넷에서 바로 불러와 분석을 시작합니다.
택시 '결제수단(payment)'을 기준으로 그룹화한 뒤, 승객들이 지불한 '총 요금(total)'에 대해 
평균(mean), 중앙값(median), 결제 건수(count)를 한 번에 계산하는 코드를 작성하세요.
"""
### 모범답안 ###
import pandas as pd

# 1. read_csv() 안에 인터넷 URL을 직접 넣어 공공데이터(뉴욕 택시 데이터)를 즉시 불러옵니다.
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df_taxis = pd.read_csv(url)

# 2. groupby()와 agg()를 사용하여 'payment'별 'total' 요금의 요약 통계를 한 번에 구하세요.
# (적용할 통계 함수: 'mean', 'median', 'count')
payment_stats = df_taxis.groupby("payment")["total"].agg(["mean", "median", "count"])

# 3. 평균 요금('mean')을 기준으로 내림차순 정렬하세요.
payment_stats = payment_stats.sort_values(by="mean", ascending=False)
print("\"--- 결제 수단별 요금 통계 ---\"")
print(payment_stats, "\n")


"""
\"문제 2. 피벗 테이블을 활용한 다차원 요금 분석 (pivot_table)\"
어느 지역에서, 어떤 색상의 택시가 돈을 많이 벌었을까요?
행(index)에는 '탑승 지역(pickup_borough)', 열(columns)에는 '택시 색상(color)'을 배치하고, 
값(values)으로는 '총 요금(total)'의 합계(sum)를 보여주는 피벗 테이블을 생성하세요.
"""
### 모범답안 ###
# 1. pivot_table()을 사용하여 지시사항에 맞는 형태의 테이블을 만드세요.
# 2. 데이터가 없는 빈칸이 발생할 경우 0으로 채우고(fill_value=0), 
# 행과 열의 총합(총계)을 추가(margins=True)하여 실무용 보고서 형태로 만드세요.
pivot_df = pd.pivot_table(
    df_taxis,
    index="pickup_borough",
    columns="color",
    values="total",
    aggfunc="sum",
    fill_value=0,
    margins=True
)

print("\"--- 탑승 지역 및 택시 색상별 요금 피벗 테이블 ---\"")
print(pivot_df, "\n")


"""
\"문제 3. 통계 기초를 활용한 지역별 변동성 분석 (분산)\"
어느 지역에서 탑승했을 때 택시 요금의 편차(기복)가 가장 심할까요? 분산(variance)을 구해서 확인해 봅니다.
'탑승 지역(pickup_borough)'별로 '총 요금(total)'의 합계(sum)와 분산(var)을 계산하고,
요금 변동성이 가장 큰 상위 3개 지역을 추출하는 코드를 작성하세요.
"""
### 모범답안 ###
# 1. groupby()와 agg()를 사용하여 'pickup_borough'별 'total'의 'sum'과 'var'를 계산하세요.
borough_variance = df_taxis.groupby("pickup_borough")["total"].agg(["sum", "var"])

# 2. 분산('var')을 기준으로 내림차순 정렬하여 매출 변동성이 큰 상위 3개를 추출하세요.
top_volatile = borough_variance.sort_values(by="var", ascending=False).head(3)

print("\"--- 요금 변동성(분산)이 가장 큰 지역 Top 3 ---\"")
print(top_volatile)