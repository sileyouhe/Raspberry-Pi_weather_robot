#这个脚本就是为了讲个古诗
import requests
from requests import exceptions
import broadcast
import json


def getGushi(flag):
    if flag == 0:        #这是推荐一句诗词的接口
        url2 = 'https://api.gushi.ci/all.json'

        try:
            response = requests.get(url=url2, timeout=3)
            response.raise_for_status()
        except exceptions.ConnectTimeout as e1:
            errorText = '找不到服务器'
            broadcast.report(errorText)
            return "Please check your connection!"
        data = response.content.decode('utf-8')
        jsondata = json.loads(data)
        author = jsondata['author']
        content = jsondata['content']
        origin = jsondata['origin']
        reportText = "%s选自%s的《%s》" % (content, author, origin)
        broadcast.report(reportText)

    else:         #整首
        url2 = 'https://v2.jinrishici.com/one.json'

        try:
            response = requests.get(url=url2, timeout=3)
            response.raise_for_status()
        except exceptions.ConnectTimeout as e1:
            errorText = '找不到服务器'
            broadcast.report(errorText)
            return "Please check your connection!"

        data = response.content.decode('utf-8')
        jsondata = json.loads(data)
        if jsondata['status'] != 'success':
            return 'error!'
        content = jsondata['data']['origin']['content'][0] + jsondata['data']['origin']['content'][1]
        title = jsondata['data']['origin']['title']
        dynasty = jsondata['data']['origin']['dynasty']
        author = jsondata['data']['origin']['author']
        print(jsondata['data']['origin']['content'])

        reportText = "给您推荐%s%s的,《%s》,%s" % (dynasty, author, title, content)
        broadcast.report(reportText)


if __name__ == '__main__':
    flag = 1
    getGushi(flag)
