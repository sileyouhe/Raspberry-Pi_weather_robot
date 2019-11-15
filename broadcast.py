#百度智能AI之语音播报
import os
import requests
import platform
weather_text = "%s今天%s转%s,%s度到%s度" % ('郑州', '小雨', '阵雨', '25', '20')

def report(text):
    reportText = text
    urlreport = "https://tsn.baidu.com/text2audio?tex="+reportText+'&lan=zh&cuid=sileyouhe&ctp=1&tok=25.efece6ea530bbff31c30d30e24e339e2.315360000.1867822678.282335-11999766'
    response = requests.get(url=urlreport)

    with open('1.mp3', 'wb') as f:
        f.write(response.content)
    if platform.system() != 'Windows':  #如果是windows系统就不能用这条指令了
        #os.system("mpg123 1.mp3")  #播放今天的天气预报
        os.system("mplayer 1.mp3")

if __name__ == '__main__':
    report(weather_text)