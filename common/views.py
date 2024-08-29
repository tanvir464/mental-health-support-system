from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from . import models
from baseapp import models as base_models
from registration import models as register_models

# Create your views here.
def resource(request) :
    pId = request.session.get("pId", '')
    user = register_models.select_loginuser_data(pId)
    data = models.select_resource_data()
    context = {
        'user' : user ,
        'data' : data ,
    }
    return render(request, "common/resources_list.html", context)

def resource_new(request) :
    if request.method == "POST":
        posterId = request.session.get('pId', '')
        title = request.POST.get("title", "")
        type = request.POST.get("type", "")
        des = request.POST.get("des", "")
        resource = request.POST.get("file", "")
        date = datetime.now().strftime("%Y-%m-%d")
        arr = (posterId, title, type, des, resource, date)
        print(arr)
        # models.insert_resource_data(arr)
        # return redirect("common:resource")
    return render(request, "common/resources_new.html")

def resource_card(request, id) :
    data = models.select_resourcecard_data(id)
    return render(request, "common/resource_card.html", {'data' : data})

def event(request) :
    user = request.session.get('pId', '')
    data = models.select_allevent_data()
    context = {
        "user" : user,
        "data" : data,
    }
    return render(request, "common/event_list.html", context)

def event_(request):
    # user = register_models.select_loginuser_data(request.session.get('pId',''))
    user = request.session.get('pId','')
    data = models.select_event_data(user)    
    context = {
        'user' : user,
        'data' : data,
    }
    print(context)
    return render(request, "common/event.html",context)

def request_event(request):
    return render(request, "common/request_event.html")

def event_card(request) :
    return render(request, "common/event_card.html")

def add_doctor(request) :
    return render(request, "common/add_doctor.html")

def schedule(request) :
    return render(request, "common/schedule.html")

def appointment_card(request,id) :
    Id = request.session.get('pId', '')
    userId = register_models.select_loginuser_data(Id)
    data,patient,specialist,fee = models.select_appointmentcard_data(id)
    context = {
        "data" : data,
        "patient" : patient,
        "specialist" : specialist,
        "fee" : fee,
        "userId" : userId
    }
    print(context)
    return render(request, "common/appointment_card.html", context)

def pending_card(request) :
    contact = request.session.get("contact", "")
    print(contact)
    data = models.select_pending_data(contact)
    print(data)
    return render(request, "common/pending_card.html", {"data" : data})

def pending_specialist(request) :
    data = models.select_pendingspecialist_data()
    if request.method == "POST" :
        action = request.POST.get("action", '')
        c = request.POST.get("c", '')
        if c == "acceptbutton" :
            base_models.update_pendinguser_data(action)
        return JsonResponse({'status': 'success'})
    return render(request, "common/pending_specialist.html", {"data" : data})
