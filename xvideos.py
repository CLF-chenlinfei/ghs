import threading
import time

import requests
import re

xvideosUrl ='https://www.xvideos.com'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'referer': 'https://www.xvideos.com/?k=%E6%8A%96%E9%9F%B3'
}

# 单个页面 传入的是单个页面的URL
def XgetOnePage(url, filename):
    try:
        resw = requests.session()
        response = resw.get(url, headers=headers)
        response.raise_for_status()
        # print(response.text)
    except Exception as e:
        print("error")
        return False

    allml = re.search(r'html5player.?setVideoHLS\(\'(.*?)\'\);', response.text).group(1)


    rs = resw.get(allml, headers=headers)
    # 切片成列表
    rs = rs.text.split('\n')
    murl = ""
    if rs[0]!= "#EXTM3U":
        print("非#EXTM3U")
        return False
    else:
        intml = 0
        # 寻找最高分辨率URL
        try:
            for index, line in enumerate(rs):
                if "EXT-X-STREAM-INF" in line:
                    maxml = re.search(r"NAME=\"(\d+)p\"", line).group(1)
                    if int(maxml) > int(intml):
                        intml = maxml
                        murl = rs[index + 1]
        except:
            print("最高分辨率URL没找到")
            return False

    if murl != "":
        # 这里是获取m3u8 文件的分辨率的url
        try:
            qurl = re.search(r'(https.*?)hls.m3u8', allml).group(1) + murl
        except:
            print("分辨率获取失败")
            print(allml)
            return False
        # 这里是获取 最高分辨Url
        vrs = resw.get(qurl, headers=headers)
        allurl = re.findall(r'hls.*?\n', vrs.text)
        # 下载视频
        for i in allurl:
            # https://hls-hw.xvideos-cdn.com/videos/hls/48/c3/95/48c395d712bb7c1ed685dce7901913fc/hls-1080p-50ac00.ts?e=1648527260&l=0&h=b1dd43a069fce0a3f005f3e257b8ad45
            vurl = re.search(r'(https.*?)hls.m3u8', allml).group(1) + i.replace("\n",
                                                                                                               "")
            video = resw.get(vurl, headers=headers).content
            with open(filename+".mp4", 'ab') as f:
                f.write(video)

# 搜索标签功能
def search(tag):
    tagurl = 'https://www.xvideos.com/?k=%s' % tag
    try:
        resw = requests.session()
        response = resw.get(tagurl, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print("无法连接网站，未翻墙？error")
        return False
    all = re.findall(r'<div id="video.*?thumbs.prepareVideo', response.text)

    for i in all:
        data = re.search(r'href=\"(.*?)\".*?title=\"(.*?)\"', i)
        addUrl = xvideosUrl+data.group(1)
        name = data.group(2)
        char_list = ['*', '|', ':', '?', '\/', '/', '<', '>', '"', '\\']
        for i in char_list:
            if i in name:
                name = name.replace(i, "_")
        yield {"name": name,
               "addUrl": addUrl}


# if __name__ == '__main__':
#
#     path = 'ff/'
#     url = "https://www.xvideos.com/video64551845/_1"
#     tag = "热舞"
#     # print("标签:%s,开始下载!" % tag)
#     tr = []
#     for i in search(tag):
#         t = threading.Thread(target=getOnePage, args=(i['addUrl'], path+i['name']))
#         t.start()
#         tr.append(t)
#         time.sleep(0.1)
#         # getOnePage(i['addUrl'], path+i['name'])
#     for i in tr:
#         i.join()
#     print("标签:%s,下载完成!" % tag)