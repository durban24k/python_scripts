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

# w.detailed_status         # 'clouds'
# w.wind()                  # {'speed': 4.6, 'deg': 330}
# w.humidity                # 87
# w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# w.rain                    # {}
# w.heat_index              # None
# w.clouds                  # 75