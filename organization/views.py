from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from . import models
from baseapp import models as base_models
from registration import models as register_models
from datetime import datetime

# Create your views here.
def index(request):
    id = request.session.get("pId", '')
    data = models.select_user_data(id)
    
    now = datetime.now()
    hr = now.hour
    wish = "Evening"
    if (5 <= hr <= 12):
        wish = "Morning"
    if (13 <= hr <= 18):
        wish = "Afternoon"
    if (19 <= hr <= 24):
        wish = "Evening"
    context = {
        'data' : data ,
        'wish' : wish
    }
    return render(request, "organization/organization_dashboard.html", context)

def list(request):
    user = request.session.get('pId', '')
    data = models.select_data()    
    context = {
        "user" : user,
        "data" : data,
    }    
    return render(request, "organization/organization_list.html", context)

def card(request, id):
    data = models.select_card_data(id)
    context = {
        "data" : data
    }
    return render(request, "organization/organization_card.html", context)

def add(request):
    if request.method == "POST" :
        name = request.POST.get('name', '')
        type = request.POST.get('type', '')
        edate = request.POST.get('edate', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        hrno = request.POST.get('hrno', '')
        country = request.POST.get('country', '')
        city = request.POST.get('city', '')
        district = request.POST.get('district', '')
        postal = request.POST.get('postal', '')
        img = request.POST.get('file', '')
        password = request.POST.get('password', '')
        cpassword = request.POST.get('cpassword', '')
        address = f'{hrno},{city},{district}-{postal},{country}'
        arr = (name,contact,email,address,edate,type,password,img)
        print(arr)
        models.insert_data(arr)
        return redirect("organization:index")
    return render(request, "organization/add_organization.html")

def events(request):
    id = request.session.get('pId', '')
    data = models.select_allevent_data(id)
    print(data)
    return render(request, "organization/events.html",{"data" : data})

def event_card(request ,id):
    user = register_models.select_loginuser_data(request.session.get('pId',''))
    data,event,fac,org = models.select_eventcard_data(id)
    epar = models.select_eventparticipant_data(id)
    parStatus = False
    for p in epar :
        if p[0] == user[0] :
            parStatus = True
            break
    context = {
        "data" : data,
        "event" : event,
        "fac" : fac,
        "org" : org,
        "user" : user,
        "epar" : epar,
        "parStatus" : parStatus,
    }
    if request.method == "POST" :
        action = request.POST.get("action", '')
        c = request.POST.get("c", '')
        participant = user[0]
        event = action      
        if c == "participate" :
            participant = user[0]
            event = action 
            arr = (event,participant)
            models.insert_participant_data(arr)
            
        elif c == "acceptbutton" :
            participant = action
            event = id 
            arr = [event,participant,1]
            print(arr)
            base_models.update_eventparticipant_data(arr)
        elif c == "rejectbutton" :
            participant = action
            event = id 
            arr = [event,participant,0]
            base_models.update_eventparticipant_data(arr)    
        return JsonResponse({'status': 'success'})                
    return render(request, "organization/orgevent_card.html", context)

def create_events(request):
    userId = request.session.get('pId', '')
    if request.method == "POST" :
        topic = request.POST.get('topic', '')
        type = request.POST.get('type', '')
        mode = request.POST.get('mode', '')
        duration = request.POST.get('duration', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        loc = request.POST.get('address', '')
        arr = (userId,topic,type,mode,date,time,loc,"description",duration)
        models.insert_event_data(arr)
    return render(request, "organization/create.html")

def workshop(request, id):
    data,faci = models.select_workshopevent_data(id)
    fac = models.select_facilitator_data()
    context = {
        "data" : data,
        "faci" : faci,
        "fac" : fac,
    }
    if request.method == "POST" :
        mode = request.POST.get('mode','')
        activity = request.POST.get('activity','')
        follow = request.POST.get('follow','')
        pre = request.POST.get('prerequisite','')
        # material = request.POST.get('file','')
        facilitator = request.POST.get('facilitator','')
        if facilitator == "Select" :
            facilitator = None
        warr = (activity,follow,pre,int(facilitator),id)
        base_models.update_workshopevent_data(warr)
    return render(request, "organization/org_workshop.html", context)

def seminar(request, id):
    data,speaker = models.select_seminarevent_data(id)
    sp = models.select_facilitator_data()
    context = {
        "data" : data,
        "sp" : sp,
    }
    if request.method == "POST" :
        mode = request.POST.get('mode','')
        agenda = request.POST.get('agenda','')
        sponshor = request.POST.get('sponshor','')
        # material = request.POST.get('file','')    
        # warr = (agenda,sponshor,id)
        # base_models.update_workshopevent_data(warr)
        c = request.POST.get('c', '')
        if c == "speaker" :
            speak = request.POST.get('data', '')
            arr = (id, speak)
            models.insert_seminarspeaker_data(arr)
            return JsonResponse({'status': 'success'})
    return render(request, "organization/org_seminar.html", context) 