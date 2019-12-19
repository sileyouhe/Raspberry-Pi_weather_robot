# Raspberry-Pi_weather_robot


Introduction
----
A entrepreneurship program from March to October in 2018

A Raspberry Pi robot 

Weather brocast, clothing recommendation, voice recognization, simple communication

Development Environment
---
python 3.7 
pycharm(windows)  
Linux (Raspberry-Pi)  

Technologies Used
----
Software:  
UI： QT5 + PYQT  
Weather Information：HeWeather API  + Python Request 
Clothing Recommendation：Python Request  + MySQL
Voice Recognization：Baidu AI API
Broadcast：Baidu AI API + mplayer(Linux)  


Hardware:
Raspberry Pi 3 Model B+ (Linux + Python3.7)  
Monitor：3.5 inch HDMI LCD  
Record：Usb Sound Card + Usb microphone + arecord 



Files Description
----
`release_first.ui`  ：Generate this UI file after designing the User Interface with **QT Creator** 

`weather_UI.py` ：Use pyqt to convert the release_first.ui file to python file

`get_weather.py`: Send a request to the **HeWeather API** and return weather information in the JSON file format

`brocast.py`：Upload the text to the **Baidu speech synthesis API**, store the synthesized speech as an MP3 file, and use **mplayer** to play on the Raspberry Pi.  

`speech_recognition.py` : Use the **arecord** command in linux to record the user commend and save the file. Upload the generated file to **Baidu speech recognition API** for identification.  

`get_recommend.py`：Send the request to our clothing recommendation server with a unique machine code, get today's recommendation



项目介绍
----
2018年大三下和大四上的一个十人项目  

能播报天气，播报当日符合天气状况的穿衣搭配推荐，支持简单语音识别和交流的机器人。

运行环境
---
python 3.7 
pycharm(windows)  
Linux (Raspberry-Pi)  

使用的库和技术
----
软件  
UI设计： QT5 + pyqt  
天气：和风天气API  + python request库  
搭配推荐：python request库从服务器数据库获取（服务器由其他项目成员负责）  
语音识别：百度语音识别库AipSpeech  
语音播报：百度在线语音合成API + mplayer(Linux)  


硬件  
树莓派 3B+ 主板  安装python3.7环境  
屏幕显示：树莓派3.5寸 HDMI显示屏 支持触控  
录音：外接声卡 + 独立麦克风 + arecord(Linux录音命令)  
触控： HTTM电容式触摸开关  


文件介绍
----
`release_first.ui`  ：使用QT creator设计想要的界面后生成ui文件  
`weather_UI.py` ：使用pyqt把release_first.ui文件转换的python代码，可以运行
`get_weather.py`: 向和风天气API发起查询天气请求，返回JSON文件格式的天气信息  
`brocast.py`：把需要播报的文字内容上传给百度语音合成API，把合成的语音存储为MP3文件，在树莓派端使用mplayer播放  
`speech_recognition.py` : 在树莓派端使用arecord命令录音并生成文件保存，把生成的文件上传到百度语音识别库AipSpeech进行识别  
`get_recommend.py`：携带机器码向服务器端发起请求，获取今日搭配推荐





