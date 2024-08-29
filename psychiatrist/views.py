from django.shortcuts import render, redirect
from . import models 
from baseapp import models as base_models
from registration import models as register_models
from datetime import date, datetime


# Create your views here.
def index(request):
    id = request.session.get("pId", '')
    data = models.select_user_data(id)
    appdata = models.select_psychiatristappointment_data(id)
    appointment = []
    for a in appdata :
        if a[6] == datetime.today().date() :
            appointment.append(a)
    now = datetime.now()
    hr = now.hour
    print(hr)
    wish = "Evening"
    if (5 <= hr <= 12):
        wish = "Morning"
    if (13 <= hr <= 18):
        wish = "Afternoon"
    if (19 <= hr <= 24):
        wish = "Evening"
    context = {
        'data' : data ,
        'app' : len(appdata) ,
        'appointment' : appointment ,
        'wish' : wish
    }
    return render(request, "psychiatrist/psychiatrist_dashboard.html", context)

def psychiatrist_list(request):
    user = request.session.get('pId', '')
    data = models.select_data()    
    context = {
        "user" : user,
        "data" : data,
    }
    return render(request, "psychiatrist/psychiatrist_list.html", context)

def appointments(request):
    id = request.session.get("pId")
    user = register_models.select_loginuser_data(id)
    if id == "admin" :
        data = base_models.select_psychiatristappointment_data()
    else:
        data = models.select_psychiatristappointment_data(id)
    context = {
        "data" : data,
        "user" : user,
    }
    if request.method == "POST" :
        action = request.POST.get("action", '')
        c = request.POST.get("c", '')
        if c == "acceptbutton" :
            base_models.update_specialistacceptappointment_data(action)            
        elif c == "rejectbutton" :            
            base_models.update_specialistrejectappointment_data(action)  
    return render(request, "psychiatrist/appointments.html", context)

def psychiatrist_card(request, id):
    userId = request.session.get("pId", '')
    user = register_models.select_loginuser_data(userId)
    data = models.select_psychiatristcard_data(id)
    app = models.select_psychiatristappointment_data(id)
    context = {
        "data" : data,
        "total_appointment" : len(app),
        "user" : user,
    }
    return render(request, "psychiatrist/psychiatrist_card.html", context)