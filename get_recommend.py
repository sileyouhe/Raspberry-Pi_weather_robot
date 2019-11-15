import requests
from requests import exceptions
import broadcast
import json

def getDapei():
    headers = {'Content-Type': 'application/json'}  #设置数据为json格式，没有这条代码就发不了

    url2 = 'http://112.74.53.233:8888/weather/weather_getInfo'
    data2 = {'jiqima': '123'}
    jsondata = json.dumps(data2)

    try:
        response = requests.post(url=url2, headers=headers, data=jsondata, timeout=3)
        response.raise_for_status()
    except exceptions.ConnectTimeout as e1:
        errorText = '找不到服务器'
        broadcast.report(errorText)
        return "Please check your connection!"
    except exceptions.HTTPError as e2:
        return "HTTP error  or invalid machine !"
    except exceptions.ConnectionError:
        return "Service closed."
    response.encoding = 'utf-8'

    if response.status_code == 200:
        # print(response.text)
        # print(response.content.decode('utf-8'))
        dapei = response.text
        reportText = "今天为您推荐的搭配是,%s" % dapei
        broadcast.report(reportText)
        return dapei
    else:
        return "Please check your network service!"

if __name__ == '__main__':
    print(getDapei())