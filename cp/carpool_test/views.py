from django.shortcuts import render
import pymysql
# Create your views here.
from carpool_test.models import Orders_af as af 
from carpool_test.models import Orders_tm as tm
from carpool_test.models import Orders_td as td
#import pandas as pd
import csv
import codecs
from django.http import HttpResponse
import datetime
import time

# 引入我们创建的表单类
#from .forms import AddForm
#################################step 1#########################

def index(request):
    return render(request,'index.html')

#################################step 2#########################
def info(request):
    back={}

    if request.POST:
        v_dir=request.POST.get('dir',False)
        v_time_p=request.POST.get('time_p',False)
        v_time=request.POST.get('time',False)
 
        if v_time_p:
            if v_dir=='GC':
                if v_time_p in "预定":
                    web='book.html'
                if v_time_p in "今天":
                    web="now.html"
                DIR='贵池'
            elif  v_dir=='QY':
                if v_time_p in "预定":
                    web='book.html'
                if v_time_p in "今天":
                    web="now.html"
                DIR='青阳'
            else:
                print("*************")
                print("404")
                web='404.html'
        back['dir']=DIR 
        back['time_p']=v_time_p
        back['time']=v_time
        
        
    return render(request,web,{'back': back})

#################################step 3#########################
#############################
#############预定模式#########
def ticket(request):
    back_info={}
    web='wait.html'
    if request.method == 'POST':
        # 当提交表单时
            print("$$$$$$$$$$$$$$")
            v_name=request.POST.get('user',False)
            v_tel=request.POST.get('tel',False)
            v_addr=request.POST.get('addr',False)
            v_time=request.POST.get('time',False)
            v_num=request.POST.get('num',False)
            day=request.POST.get('day',False)
            to_where=request.POST.get('to_where',False)
        #cur=datetime.datetime.now()   #获取当前系统时间
            post=time.strftime("%m:%d")#和今天的不同，只取得今天的值，方便定时调取
            print(v_addr)
        #获取id，update数据
            if day in '明天':
                #print("hey I am going to choose time")
                twz = tm.objects.create(Name=v_name, Tel=v_tel,Addr=v_addr,Time=v_time,Post=post,To_where=to_where,Num=v_num)
            elif day in '后天':
                #print("hey I am going to choose time")
                twz = af.objects.create(Name=v_name, Tel=v_tel,Addr=v_addr,Time=v_time,Post=post,To_where=to_where,Num=v_num)
            #显示订单信息
            back_info['user']=v_name
            back_info['tel']=v_tel
            back_info['addr']=v_addr
            back_info['time']=v_time
            back_info['num']=v_num
            back_info['to_where']=to_where

            twz.save()

    
    return render(request,web,{'info': back_info})
########################################
############今天的即时下单##############
#######################################

def now(request):
    web='last_info.html'
    back_info={}
    if request.method == 'POST':
        # 当提交表单时
            v_name=request.POST.get('user',False)
            v_tel=request.POST.get('tel',False)
            v_addr=request.POST.get('addr',False)
            v_time=request.POST.get('time',False)
            v_num=request.POST.get('num',False)
            #day=request.POST.get('day',False)
            to_where=request.POST.get('to_where',False)
        #cur=datetime.datetime.now()   #获取当前系统时间
            post=time.strftime("%m:%d:%H:%M:%S")

        #插入今天的表单
          
            today=td.objects.create(Name=v_name, Tel=v_tel,Addr=v_addr,Time=v_time,Post=post,To_where=to_where,Num=v_num)
        #twz= Orders.objects.create(Name=v_name, Tel=v_tel,Addr=v_addr,Time=v_time,Post=post)
            today.save()
            back_info['user']=v_name
            back_info['tel']=v_tel
            back_info['addr']=v_addr
            back_info['time']=v_time
            back_info['num']=v_num
            back_info['to_where']=to_where
            back_info['posttime']=post

    return render(request,web,{'info': back_info})
  
#################################step 4（last——info才有）#########################
import json
import requests

class WeChatPub:
    s = requests.session()
    token = None

    def __init__(self):
        self.token = self.get_token("wwf446799bff4f1ecc", "m8q4yR1QQ01xIjaMFz4F0uL-jwaN9o6InOFyUEc-U00")
        print("token is " + self.token)

    def get_token(self, corpid, secret):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwf446799bff4f1ecc&corpsecret=m8q4yR1QQ01xIjaMFz4F0uL-jwaN9o6InOFyUEc-U00"
        rep = self.s.get(url)
        print("567$$$$$$$$$$$$$$$$$$$$$$$4")
        print(rep)
        if rep.status_code == 200:
            
            print(rep.text)
            return json.loads(rep.text)['access_token']
        else:
            print("request failed.")
            return None

    def send_msg(self,content,tel):

        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + self.token
        header = {
            "Content-Type": "application/json"
        }
        form_data = {
            "touser": "@all",
            "toparty": " PartyID1 | PartyID2 ",
            "totag": " TagID1 | TagID2 ",
            "msgtype": "textcard",
            "agentid": 1000002,
            "textcard": {
                "title": "来订单啦",
                "description": content,
                "url": "49.234.72.99/tel/"+tel,
                "btntxt": "更多"
            },
            "safe": 0
        }
        print("^^^^^^^^^^^^^^^^^^")
        print(type(form_data))
        print(form_data['textcard']['url'])
        rep = self.s.post(url, data=json.dumps(form_data).encode('utf-8'), headers=header)
        if rep.status_code == 200:
            return json.loads(rep.text)
        else:
            print("request failed.")
            return None


def wx(request,):
  web="wait_now.html"
  if request.method == 'POST':
    name=request.POST.get('user',False)
    tel=request.POST.get('tel',False)
    addr=request.POST.get('addr',False)
    time=request.POST.get('time',False)
    num=request.POST.get('num',False)
    to_where=request.POST.get('to_where',False)
    posttime=request.POST.get('posttime',False)
    #print("****************")
    #print(type(posttime))
    #print(posttime)
    wechat = WeChatPub()
    #
    content_to="<div class=\"red\">去："+to_where+"</div> "
    content_name="<div class=\"black\">乘客姓名："+name+"</div> "
    content_addr="<div class=\"black\">上车地点："+addr+"</div> "
    content_num="<div class=\"black\">人数："+num+"人</div> "
    content_time="<div class=\"black\">上车时间："+time+"</div> "
    content_tel="<div class=\"black\">乘客电话："+tel+"</div> "
    info="<div class=\"black\">请尽快联系乘客，师傅辛苦啦！</div> "
   
    content=content_to+content_name+content_addr+content_num+content_time+content_tel+info
    wechat.send_msg(content,tel)



    return render(request,web)
#######################################################
#######################################################
#######################################################
def Tel_copy(request,tel):
  #new_data=td.objects.filter(book_id=book_id).order_by('-id')[:1]
  web="tel.html"
  #Tel=request.GET['tel']
  print("&&&&&&&&&&&&&&&&&&&&&&")
  print(tel)
  #data=td.objects.all() 
  #lenght=data.count()
  #result=td.objects.filter(Post=posttime)
  print("&&&&&&&&&&&&&&&&&&&&&&")
  #print(result)
  back={}
  back['tel']=tel


  return render(request,web,{'tel': tel})

  
#######################################################
#############TEST###############################
#######################################################


def Test(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="预定名单.csv"'
    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response)#

    web="tel.html"
    sys_time=time.strftime("%m:%d")#今天的时间
    #day=int(sys_time[-2:])
    print(sys_time)
    tm_order=tm.objects.filter(Post=sys_time).order_by('Time')#取得今天提交的日子
    #tm_order=tm.objects.filter(Num=1).order_by('Time')#取得今天提交的日子
    print(tm_order)
    GC={}
    QY={}
    flag=['0']
    for i in tm_order:
        to=i.To_where
        print("&&&&&&&")
       # print(type(flag[0]))
        f=int(flag[0])+1
        flag[0]=str(f)
        writer.writerow(flag)#写入第几位乘客
        if '贵池' in to:
            GC['乘客电话'] = i.Tel
            GC['乘客姓名'] = i.Name
            GC['上车时间'] = i.Time
            GC['人数'] = i.Num
            GC['上车地点'] = i.Addr
            writer.writerow(['去贵池'])#写入去向
            for key,value in GC.items():
              writer.writerow([key, value])
        else:
            QY['乘客电话'] = i.Tel
            QY['乘客姓名'] = i.Name
            QY['上车时间'] = i.Time
            QY['人数'] = i.Num
            QY['人数'] = i.Addr
            writer.writerow(['去青阳'])#写入去向
            for key,value in QY.items():
              writer.writerow([key, value])
        
    writer.writerow(['今天的预定名单已经结束了！！！请及时联系乘客'])
    #print(GC)
   
    return response
   # writer = pd.ExcelWriter('/home/coding/workspace/cp/o1.xlsx')
   # df1 = pd.DataFrame(data=GC)
   # df1.to_excel(writer,encoding='utf-8')
   # writer.save()
     

   # return render(request,web,{'tel':GC})