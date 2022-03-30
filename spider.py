import requests
import os
import re
import json


from pixivcookie import load_cookies

cook = load_cookies()
header = {
    "referer": "https://www.pixiv.net/",
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36x-requested-with: XMLHttpRequest'
}

def PV_Get_All_id(id):
    try:
        fiurl = "https://www.pixiv.net/users/%s" % id
        url = "https://www.pixiv.net/ajax/user/%s/profile/all?lang=zh" % id
        req = requests.session()
        js = req.get(url, headers=header, cookies=cook).json()
        html = req.get(fiurl, headers=header, cookies=cook).text
        filename = re.search(r"\"userId\".*?\"name\":\"(.*?)\"", html).group(1)

        t1 = (js["body"]["illusts"], filename)
        return t1
    except:
        print("获取所有ID失败!")
        return False


# PV_Get_All_id("3384404")
# PV_Get_All_id("9459043")