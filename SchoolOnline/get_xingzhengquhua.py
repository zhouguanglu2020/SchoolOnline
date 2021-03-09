# -*- coding: utf-8 -*-
"""
@Time : 2021/3/9 17:04
@Author : Administrator
@Email : zhouguanglu2012@163.com
@File : get_xingzhengquhua.py
@Project : SchoolOnline
@Description：
"""
import urllib3,json
def get_xingzhengquhua(url_link):
    ##高德地图行政区划获取URL
    http = urllib3.PoolManager()
    #发送请求
    res = http.request("GET",url_link)
    back_data_json = res.data.decode()
    back_data = json.loads(back_data_json)
    print(back_data["districts"][0]["districts"])


GAODE_API_XingZhengQuHua = "https://restapi.amap.com/v3/config/district?keywords=%E4%B8%AD%E5%9B%BD&subdistrict=3&key=fa631b2f4aa95d105bc0fb8ec6ab791c"
get_xingzhengquhua(GAODE_API_XingZhengQuHua)