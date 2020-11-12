from pyowm import OWM # 오픈 웨더 맵 api 사용하는 라이브러리 임포트

k2c = lambda k: k - 273.15
API_KEY = "0ac1a5333945db74b5208732d0e43725" # api 키 

owm = OWM(API_KEY) # owm 앱 만듦, api 키로

mgr = owm.weather_manager() # weather manager 라는 owm 안에 있는 것(매니져) 만듬ㄹ

obs = mgr.weather_at_place('Seoul,KR') # 서울의 날씨 mgr로 가져옴 obs -> observation
weather = obs.weather # obs중에 wheater를 가져옴
temp = weather.temperature() # 온도 관련 dict 가져옴
print(weather.detailed_status) # 이건 이제 지금 코드 기준 서울의 구체적인 상태
# 구체적인거 싫으면 weather.status 프린트하면댐
print("최대 온도:", k2c(temp["temp_max"])) # 이건 온도 관련 dict (weather 변수)의 키중 하나인 temp_max (최대 온도) 가져옴
print("최소 온도:", k2c(temp["temp_min"])) # 이건 위와 똑같이 최저 온도

# for i in temp:
#  print(i)
# 하면 temp의 키를 가져올수 있음