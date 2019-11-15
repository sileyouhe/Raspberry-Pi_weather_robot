import requests
from requests import exceptions
import json
import broadcast
def GetTianqi():
    url = "https://free-api.heweather.com/s6/weather/forecast?location=郑州&key=81b31f9177444f7f8bec2ba9ed811a07"
    try:
        response = requests.get(url=url, timeout=3)
    except exceptions.ConnectTimeout as e1:
        errorText = '找不到服务器'
        broadcast.report(errorText)
        return "Please check your connection!"
    except exceptions.HTTPError as e2:
        return "Please check your HTTP!"


    rawdata = response.text
    jsondata = json.loads(rawdata)

    data = jsondata['HeWeather6'][0]
    #print(data)
    city = data['basic']['location']
    date1 = data['daily_forecast'][0]['date']
    tmp_max = data['daily_forecast'][0]['tmp_max']
    tmp_min = data['daily_forecast'][0]['tmp_min']
    tianqi_d = data['daily_forecast'][0]['cond_txt_d']
    tianqi_n = data['daily_forecast'][0]['cond_txt_n']

    today = [200, city, date1, tmp_max, tmp_min, tianqi_d, tianqi_n]
    if tianqi_d != tianqi_n:
        reportText = "今天是%s,%s今天%s转%s,最低气温%s度,最高气温%s度" % (date1, city, tianqi_d, tianqi_n, tmp_min, tmp_max)
    else:
        reportText = "今天是%s,%s今天全天%s,最低气温%s度,最高气温%s度" % (date1, city, tianqi_d, tmp_min, tmp_max)
    broadcast.report(reportText)
    #先把当日的语音播报做出来
    #date2 = data['daily_forecast'][1]['date']
    #date3 = data['daily_forecast'][2]['date']
    #print(today)
    return today

if __name__ == '__main__':
    GetTianqi()