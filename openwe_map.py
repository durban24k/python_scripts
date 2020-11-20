# OPEN WEATHER MAP API SCRIPT
import pyowm
from keys import owm_api

api_key=owm_api['key']
owm=pyowm.OWM(api_key)
mgr=owm.weather_manager()
place=mgr.weather_at_place('Nairobi')
w=place.weather
temp=w.temperature('celsius')

print(temp)