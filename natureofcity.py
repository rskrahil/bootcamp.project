import requests
#import os
from datetime import datetime

api_key = 'ba554b9e15672fbb749c040d881bdce6'
location = input("Enter the city or state name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#declaring variable
temp_city = ((api_data['main']['temp']) - 273)
weather_desc =api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#declaring dictionary to print info
nature = {'Temp':temp_city, 'Weather':weather_desc, 'Humidity':hmdt, 'Wind':wind_spd, 'Date&Time':date_time}

print ("******************************************")
print ("Nature of city :- {} !! {}" .format(location.upper(), nature['Date&Time']))
print ("******************************************")

print ("Current Temperature is: {:.2f} deg C".format(nature['Temp']))
print ("{},{} \n".format("Current Weather desc :" ,nature['Weather']))
print ("{},{},{} \n".format("Current Humidity :",nature['Humidity'] ,"%"))
print ("{},{},{} \n".format("Current iWind Speed :", nature['Wind'], "kmph"))

print ("******************************************")

