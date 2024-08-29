from django.http import JsonResponse
from django.shortcuts import render
from . import models
from baseapp import models as base_models
from registration import models as register_models
from datetime import datetime

# Create your views here.

def index(request) :
    id = request.session.get('pId', '')
    data = models.select_centercard_data(id)
    app = models.select_appointmentcenter_data(id)
    appointment = []
    for a in app :
        if a[0] == datetime.today().date() :
            appointment.append(a)
    context = {
        "data" : data,
        "appointment" : appointment,
    }
    print(context)
    if request.method == "POST" :
        c = request.POST.get("c","")        
        action = request.POST.get('action','')
        print(c,action)
        if c == "acceptbutton" :
            base_models.update_centerappointment_data(action) 
            return JsonResponse({"status" : "success"})
    
    return render(request,"diagnosis/diagnostic_dashboard.html", context)

def appointment(request) :
    id = request.session.get("pId", '')
    data = models.select_appointmentcenter_data(id)
    report = models.select_reportdone_data(id)
    context = {
        "data" : data ,
        "report" : report,
    }
    if request.method == "POST" :
        c = request.POST.get("c","")        
        action = request.POST.get('action','')
        if c == "acceptbutton" :
            base_models.update_centerappointment_data(action)            
        elif c == "donebutton" :
            base_models.update_reportdone_data(action)
        return JsonResponse({"status" : "success"})
    return render(request, "diagnosis/appointment.html", context)

def add(request) :
    if request.method == "POST" :
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        contact = request.POST.get("contact","")
        address = request.POST.get("address","")                
        password = request.POST.get("password","")                
        cpassword = request.POST.get("cpassword","")
        arr = (name,contact,email,address,password)
        if password == cpassword :
            print(arr)      
            models.insert_data(arr)
    return render(request, "diagnosis/add_center.html")

def list(request) :
    user = request.session.get("pId", '')
    data = models.select_data()
    context = {
        "user" : user,
        "data" : data,
    }
    return render(request, "diagnosis/diagnostic_list.html", context)

def card(request, id) :
    data = models.select_centercard_data(id)
    context = {
        "data" : data,
    }
    return render(request, "diagnosis/diagnostic_card.html", context)

def make_appointment(request,id) :
    data = models.select_data()
    context = {
        "id" : id,
        "data" : data,
    }
    if request.method == "POST" :
        centerId = request.POST.get("centerId", '')
        date = request.POST.get("date", '')
        time = request.POST.get("time", '')
        arr = (id,centerId,date,time)
        print(arr)
        models.insert_appointment_data(arr)        
    return render(request, "diagnosis/make_appointment.html",context)

def report(request, id = 1) :
    data = models.select_appointmentreport_data(1)
    if request.method == "POST" :
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        report = request.POST.get('file', '')
        arr = (data[0],date,time,report)
        models.insert_report_data(arr)
    return render(request, "diagnosis/create_report.html",{'data' : data})

def report_card(request, id) :
    user = register_models.select_loginuser_data(request.session.get('pId', ''))
    data = models.select_reportcard_data(id)
    context = {
        "data" : data,
        "user" : user,
    }
    return render(request, "diagnosis/report_card.html", context)