#coding:utf-8
#作者：武晓坤
#时间:2016-01-22
import urllib2
import urllib
import ssl
import json
import time
#ssl._create_default_https_context = ssl._create_unverified_context 
opt = "q"
while opt == "q":
  
  opt = raw_input("Please input the option:")

  from_st = raw_input("Input Start:").upper()

  to_st = raw_input("Destination:").upper()

  train_date = raw_input("Time:")

  n = int(raw_input("Number:"))

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

  i = 1
  for i in range(n):
    print 'The ' + str(i) + " times!"
    print '=' * 42
    #头列表
    print "Total num: "+ str(train_num) + "  Time: " + search_date.encode("utf-8") + "  Start-city: " + from_city.encode("utf-8") + "  Destynation: " + to_city.encode("utf-8")
    print '=' * 42
    #车次列表
    format_data = "%-6s%-6s%-6s%-6s%5s%6s%6s"
    print format_data % ("TCode","Stime","Atime","Lishi","SBed","HBed","HSeat")
    for i in range(train_num):
      if trains[i]["yw_num"] == "无".decode("utf-8"):
         trains[i]["yw_num"] = "--"
      if trains[i]["rw_num"] == "无".decode("utf-8"):
         trains[i]["rw_num"] = "--"
      if trains[i]["yz_num"] == "无".decode("utf-8"):
         trains[i]["yz_num"] = "--"
      print format_data % (trains[i]["station_train_code"],trains[i]["start_time"],trains[i]["arrive_time"],trains[i]["lishi"],trains[i]["rw_num"],trains[i]["yw_num"],trains[i]["yz_num"])
    time.sleep(2) 
raw_input('please input enter to exit!')


