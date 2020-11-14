from pyowm import OWM 

k2c = lambda k: k - 273.15
API_KEY = "0ac1a5333945db74b5208732d0e43725" 
owm = OWM(API_KEY) 

mgr = owm.weather_manager() 
obs = mgr.weather_at_place('Seoul,KR') 
weather = obs.weather
temp = weather.temperature() 
print(weather.detailed_status) 

print("최대 온도:", k2c(temp["temp_max"])) 
print("최소 온도:", k2c(temp["temp_min"])) 

