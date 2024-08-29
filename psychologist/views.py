from django.shortcuts import render, redirect
from . import models 
from baseapp import models as base_models
from registration import models as register_models
from datetime import datetime

# Create your views here.
def index(request):
    id = request.session.get("pId", '')
    data = models.select_user_data(id)
    appdata = models.select_psychologistappointment_data(id)
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
        'appointment' : appdata ,
        'wish' : wish
    }
    return render(request, "psychologist/psychologist_dashboard.html", context)

def psychologist_list(request):
    user = request.session.get('pId', '')
    data = models.select_data()    
    context = {
        "user" : user,
        "data" : data,
    }
    return render(request, "psychologist/psychologist_list.html", context)

def appointments(request):
    id = request.session.get("pId")
    user = register_models.select_loginuser_data(id)
    if id == "admin" :
        data = base_models.select_psychologistappointment_data()
    else :
        data = models.select_psychologistappointment_data(id)
    context = {
        "data" : data,
        "user" : user,
    }
    if request.method == "POST" :
        action = request.POST.get("action", '')
        c = request.POST.get("c", '')
        print(action)
        if c == "acceptbutton" :
            base_models.update_specialistacceptappointment_data(action)                        
        elif c == "rejectbutton" :            
            base_models.update_specialistrejectappointment_data(action)            
    return render(request, "psychologist/appointments.html", context)

def psychologist_card(request, id):
    data = models.select_psychologistcard_data(id)
    app = models.select_psychologistappointment_data(id)
    context = {
        "data" : data,
        "total_appointment" : len(app),
    }
    print(context)
    return render(request, "psychologist/psychologist_card.html", context)