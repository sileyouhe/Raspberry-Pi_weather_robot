from aip import AipSpeech
import platform,os
import get_weather
import get_recommend
import broadcast
import get_poem
#格式支持：pcm（不压缩）、
# wav（不压缩，pcm编码）、
# amr（压缩格式）。
# 推荐pcm 采样率 ：16000 固定值。 编码：16bit 位深的单声道。
#百度智能AI之语音识别
#思路：跑linux自带的录音软件，5秒后在当前路径产生一个wav文件，然后上传给百度进行识别,返回result里的字符串
""" 你的 APPID AK SK """
APP_ID = '11999766'
API_KEY = 'REDacf6fNMwoHXGdQxZpxHOz'
SECRET_KEY = 'jkSiDQZA7VFoDHsPY7KIXKbUpuKeoZbo'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#启动录音
def record():
    if platform.system() != 'Windows':  #如果是windows系统就不能用这条指令了
        #os.system("mpg123 1.mp3")  #播放今天的天气预报
        os.system("arecord -d 4 -f S16_LE -r 16000 -c 1 2.wav")
#启动对录音的识别
def shibie():
    # 需要识别的录音文件放在本地的2.wav
    result = client.asr(get_file_content('2.wav'), 'wav', 16000, {
        'cuid': 'sileyouhe',
        'dev_pid': 1536,
    })

    if result['err_no'] == 0:
        #print(result)
        #print(result['result'][0])
        res = result['result'][0]
        #到时候从这里拿到返回的结果
        #如果“天气”或“搭配”存在于这个字符串
        #就执行某些操作（跑那两个脚本）
        print(res)
        if '天气' in res:
            get_weather.GetTianqi()
        elif '搭配' in res:
            get_recommend.getDapei()
        elif '诗' in res:
            print(res)
            if ('一句' or '短') in res:
                get_poem.getGushi(0)  #传0进去只念一句
            else:
                get_poem.getGushi(1)
        else:
            info = "机器人没有听懂，请您再试一遍吧"
            broadcast.report(info)
    else:
        info = "机器人没有听懂，请您再试一遍吧"
        broadcast.report(info)
        print('error occurred')

if __name__ == '__main__':
    shibie()





