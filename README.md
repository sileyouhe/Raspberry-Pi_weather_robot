# Raspberry-Pi_weather_robot


项目介绍
----
能播报天气，播报当日符合天气状况的穿衣搭配推荐，支持简单语音识别和交流的机器人。

运行环境
---
python 3.7 
pycharm(windows)  
Linux (Raspberry-Pi)  

技术：
----
软件  
UI： QT5 + pyqt  
天气：和风天气API  + python request库
搭配推荐：python request库从服务器数据库获取（服务器由其他项目成员负责）  
语音识别：百度语音识别库AipSpeech  
语音播报：百度在线语音合成API + mplayer(Linux)  


硬件  
树莓派 3B+ 主板  安装python3.7环境  
屏幕显示：树莓派3.5寸 HDMI显示屏 支持触控  
录音：外接声卡 + 独立麦克风 + arecord(Linux录音命令)  
触控： HTTM电容式触摸开关  


文件介绍：
----
weather_UI.py ：使用QT creator设计想要的界面，生成ui文件，再使用pyqt把ui文件转换成python代码  
get_weather.py: 向和风天气API发起查询天气请求，返回JSON文件格式的天气信息  
brocast.py：把需要播报的文字内容上传给百度语音合成API，把合成的语音存储为MP3文件，在树莓派端使用mplayer播放  
speech_recognition.py : 在树莓派端使用arecord命令录音并生成文件保存，把生成的文件上传到百度语音识别库AipSpeech进行识别  
get_recommend.py：携带机器码向服务器端发起请求，获取今日搭配推荐





