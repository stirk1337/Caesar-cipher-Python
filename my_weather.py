import pyowm
currcity = "Екатеринбург"

def weather():
	global currcity
	weather = []
	owm = pyowm.OWM('fbee165d5e5cc25bcfa5b036701304f5', language = 'ru')
	city = owm.weather_at_place(currcity)
	w = city.get_weather()
	weather.append(w.get_temperature('celsius')['temp'])
	weather.append(w.get_detailed_status())
	return weather
	