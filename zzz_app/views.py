from django.shortcuts import render
from datetime import datetime
from pytz import timezone
# Create your views here.

def home(request):
    return render(request,'index.html')

def sleep(request):
    return render(request,'sleep_time.html')
def wake(request):
    return render(request,'wakeup_time.html')
def wakeup(request):
    times = []
    if 'pmam' in request.GET and 'hour' in request.GET and 'time' in request.GET:
        ampm = str(request.GET['pmam'])
        hour = int(request.GET['hour'])
        minute =int(request.GET['time'])
        textt ="%s %d 시 %d 분에 일어나고 싶다면"%(ampm,hour,minute)
        ampm,hour,minute = cal2(ampm,hour,minute,15)
        for i in range(6):
            ampm,hour,minute = cal2(ampm,hour,minute,90)
            times+=["%s %d : %d"%(ampm if hour!=12 else "오전" if ampm=="오후" else "오후",hour,minute)]
        times+=[textt]
        times.reverse()
    else:
        times+=["올바른 시간을 입력해 주세요!!"]
    return render(request,'result2.html',{'times':times})

def now(request):
    times = []
    if 'pmam' in request.GET and 'hour' in request.GET and 'time' in request.GET:
        ampm = str(request.GET['pmam'])
        hour = int(request.GET['hour'])
        minute =int(request.GET['time'])
        times+=["%s %d 시 %d 분에 침대에 누우면.."%(ampm,hour,minute)]
    elif 'pmam' in request.GET or 'hour' in request.GET or 'time' in request.GET:
        times+=["올바른 시간을 입력해 주세요!!"]
        return render(request,'result.html',{'times':times})
    else:
        now = datetime.now(timezone('Asia/Seoul'))
        ampm = "오전"
        if now.hour>=12:
            ampm="오후"
            hour = now.hour-12
        else:
            hour= now.hour
        minute = now.minute

    ampm,hour,minute = cal(ampm,hour,minute,15)
    for i in range(6):
        ampm,hour,minute = cal(ampm,hour,minute,90)
        times+=["%s %d : %d"%(ampm if hour!=12 else "오전" if ampm=="오후" else "오후",hour,minute)]
    return render(request,'result.html',{'times':times})

def cal(ampm,hour,minute,num):
    minute +=num
    while minute>=60:
        minute-=60
        hour+=1
    while hour>12:
        hour-=12
        ampm="오전" if ampm=="오후" else "오후"
    return ampm,hour,minute
def cal2(ampm,hour,minute,num):
    minute -=num
    while minute<0:
        minute+=60
        hour-=1
    while hour<0:
        hour+=12
        ampm="오전" if ampm=="오후" else "오후"
    return ampm,hour,minute
    
