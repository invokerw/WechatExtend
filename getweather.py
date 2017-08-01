#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import urllib2
import json
import sys

reload(sys)
sys.setdefaultencoding("utf8")

def get_today_weather(placeCode):
    url = u'http://wthrcdn.etouch.cn/weather_mini?citykey=' + str(placeCode)
	
    try:
        jsonStr = requests.get(url).text
        data = json.loads(jsonStr.encode('utf-8'))
        weather = data['data']
        return weather
    except:
        return
# 101010100 北京 
# 101020100 上海 
# 101030100 天津 
def main():
    weather = get_today_weather(101010100)
    print("city:" + weather["city"])
    print("prompt:"+weather["ganmao"])
    for x in weather["forecast"]:
        print(x["date"]+" "+x["type"]+" "+x["high"]+" "+
			x["low"]+" "+x["fengxiang"]+" "+x["fengli"])

if __name__ == '__main__':
	main()


#下面也是一个可以获取天气的代码
#weatherHtml = urllib2.urlopen('http://www.weather.com.cn/data/sk/101290201.html').read()  
#weatherJSON = json.JSONDecoder().decode(weatherHtml)  
#weatherInfo = weatherJSON['weatherinfo']  
#print('城市:' + weatherInfo['city'])
#print('城市ID:' + weatherInfo['cityid'])
#print('温度:' + weatherInfo['temp'])  
#print('风向:' + weatherInfo['WD'])  
#print('风速:' + weatherInfo['WS'])  
#print('SD:' + weatherInfo['SD'])  
#print('WSE:' + weatherInfo['WSE'])  
#print('时间:' + weatherInfo['time'])  
#print('isRadar:' + weatherInfo['isRadar'])  
#print('Radar:' + weatherInfo['Radar'])  
#print('njd:' + weatherInfo['njd'])  
#print('qy:' + weatherInfo['qy'])  
#print('rain:' + weatherInfo['rain'])  

