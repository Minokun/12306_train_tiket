#coding:utf-8
#作者：武晓坤
#时间:2016-01-22
#简介：本版本是最初原版
import urllib2
import urllib
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context 

from_st = raw_input("请输入出发城市:".decode('utf-8').encode('gbk')).upper()

to_st = raw_input("请输入到达城市:".decode('utf-8').encode('gbk')).upper()

train_date = "2016-02-12"

url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=' + train_date + '&from_station=' + from_st + '&to_station=' + to_st

headers = {       
    "GET":url,
    "Host": "kyfw.12306.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
    "Referer":"https://kyfw.12306.cn/otn/leftTicket/init"
    }

req = urllib2.Request(url)

for key in headers:
    req.add_header(key,headers[key])
    
html = urllib2.urlopen(req).read()

result = json.loads(html)

trains = result['data']['datas'] #列车的源数据序列

train_num = len(trains) #共有多少趟车

start_date = trains[1]['start_train_date']  #出发时间

from_city = trains[1]['from_station_name']  #出发城市

to_city = trains[1]['to_station_name']   #到达城市

search_date = result['data']['searchDate']  #搜索时的日期

search_date = search_date.replace("&nbsp;","-")

if start_date == '' :

    start_date = trains[0]['start_train_date']

    from_city = trains[0]['from_station_name']

    to_city = trains[0]['from_station_name']

start_date = start_date[0:4] + '-' + start_date[4:6] + '-' + start_date[6:8] #出发日期

print '=' * 80

#头列表
print "共有车次: " + str(train_num) + "  搜索时间: " + search_date.encode("utf-8") + "  出发城市: " + from_city.encode("utf-8") + "  到达城市: " + to_city.encode("utf-8")

print '=' * 80

#车次列表
data_format = "%-13s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s"
item_format = "%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s"
print data_format % ("车次","始发站","终点站","出发时间","到达时间","历时","软卧","软座","硬卧","硬座","无座")

for i in range(train_num):
    print item_format % (trains[i]["station_train_code"],trains[i]["start_station_name"],trains[i]["end_station_name"],trains[i]["start_time"],trains[i]["arrive_time"],trains[i]["lishi"],trains[i]["rw_num"],trains[i]["rz_num"],trains[i]["yw_num"],trains[i]["yz_num"],trains[i]["wz_num"],)

raw_input('please input enter to exit!')


