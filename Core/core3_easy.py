# ==========================================
# [AXIS Core반] 3회차 문제 (실전 공공데이터)
# ==========================================
"""
"문제 1. 중복 데이터 제거 및 결측치 처리"
뉴욕시 택시 운행 공공데이터를 불러와 전처리를 시작합니다.
실무 데이터에는 시스템 오류로 인한 중복 데이터나 누락된 결측치가 흔하게 존재합니다.
중복된 행을 완벽히 제거하고, 승객 수('passengers') 컬럼의 결측치는 '중앙값(median)'으로 대체한 뒤,
결제 수단('payment') 정보가 누락된 행은 분석에서 완전히 제외(삭제)하는 코드를 작성하세요.
"""
### 모범답안 ###
import pandas as pd

# 1. 인터넷 URL을 통해 뉴욕 택시 공공데이터를 즉시 불러옵니다.
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df_taxis = pd.read_csv(url)

# 2. drop_duplicates()를 사용하여 모든 열의 값이 일치하는 중복 데이터를 제거하세요. 
# (원본 데이터에 바로 반영되도록 inplace=True 옵션을 사용하세요.)
df_taxis.drop_duplicates(inplace=True)

# 3. fillna()를 사용하여 'passengers' 컬럼의 결측치를 해당 컬럼의 중앙값으로 채우세요.
passengers_median = df_taxis["passengers"].median()
df_taxis["passengers"] = df_taxis["passengers"].fillna(passengers_median)

# 4. dropna()를 사용하여 'payment' 컬럼에 결측치가 있는 행만 특정하여 제거하세요. 
# (subset 파라미터 활용)
df_taxis.dropna(subset=["payment"], inplace=True)

# 5. 전처리가 완료된 데이터의 결측치 총합을 확인하여 0이 나오는지 점검하세요.
print("--- 결측치 처리 결과 확인 ---")
print(df_taxis.isnull().sum(), "\n")


"""
"문제 2. 문자열 데이터 정리 및 데이터 타입 변환"
데이터 분석을 위해서는 데이터의 타입(Type)이 알맞게 설정되어 있어야 합니다.
택시 탑승 시간('pickup') 컬럼은 현재 단순 문자열(object)로 되어 있고, 총 요금('total')은 소수점(float) 형태입니다.
'pickup' 컬럼을 시계열 데이터(datetime)로 변환하고, 'total' 요금은 정수형(int)으로 변환하세요.
추가로 탑승 구역('pickup_zone') 이름에 포함된 공백(띄어쓰기)을 모두 언더바('_')로 치환하세요.
"""
### 모범답안 ###
# 1. pd.to_datetime()을 사용하여 'pickup' 컬럼을 datetime 타입으로 변환하세요.
df_taxis["pickup"] = pd.to_datetime(df_taxis["pickup"])

# 2. astype()을 사용하여 'total' 컬럼의 데이터 타입을 정수형(int)으로 변환하세요.
df_taxis["total"] = df_taxis["total"].astype(int)

# 3. str.replace()를 사용하여 'pickup_zone' 컬럼 내부의 공백(" ")을 언더바("_")로 대체하세요.
df_taxis["pickup_zone"] = df_taxis["pickup_zone"].str.replace(" ", "_", regex=False)

# 4. info() 메서드와 head()를 호출하여 데이터 타입과 문자열이 정상적으로 변환되었는지 확인하세요.
print("--- 데이터 타입 변환 결과 확인 ---")
df_taxis.info()
print(df_taxis[["pickup", "total", "pickup_zone"]].head(), "\n")


"""
"문제 3. 통계적 기법(IQR)을 활용한 이상치(Outlier) 제거"
총 요금('total') 데이터 중에는 장거리 운행이나 팁(Tip) 과다 지불 등으로 인해 정상 범위를 크게 벗어난 이상치가 존재할 수 있습니다.
사분위수 범위(IQR) 방식을 사용하여 'total' 요금의 극단적인 이상치를 탐지하고, 
정상 범위 내의 데이터만 추출하여 'df_clean'이라는 새로운 데이터프레임으로 저장하는 코드를 작성하세요.
"""
### 모범답안 ###
# 1. quantile()을 사용하여 'total' 요금의 1사분위수(Q1, 25%)와 3사분위수(Q3, 75%)를 각각 구하세요.
Q1 = df_taxis["total"].quantile(0.25)
Q3 = df_taxis["total"].quantile(0.75)

# 2. 사분위수 범위(IQR)를 계산하세요. (Q3에서 Q1을 뺀 값)
IQR = Q3 - Q1

# 3. 통계적 정상 데이터의 하한선(Q1 - 1.5 * IQR)과 상한선(Q3 + 1.5 * IQR)을 구하세요.
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 4. 불리언 인덱싱을 사용하여 하한선 이상, 상한선 이하인 정상 데이터만 추출하여 'df_clean'에 저장하세요.
condition = (df_taxis["total"] >= lower_bound) & (df_taxis["total"] <= upper_bound)
df_clean = df_taxis[condition]

# 5. 이상치가 제거되기 전과 후의 데이터 행(row) 개수를 출력하여 몇 개의 이상치가 제거되었는지 비교해 보세요.
print("--- IQR 이상치 제거 결과 ---")
print(f"이상치 제거 전 전체 데이터 수: {len(df_taxis)}")
print(f"이상치 제거 후 정상 데이터 수: {len(df_clean)}")