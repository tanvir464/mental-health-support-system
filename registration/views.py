from django.shortcuts import render , redirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from . import models
import patient.models, psychiatrist.models, psychologist.models



# Create your views here.
def login(request) :
    if request.method == 'POST' :
          contact = request.POST.get("contact", '')
          password = request.POST.get("password", '')
          if contact == "admin" :
                data = models.select_adminlogin_data(contact,password)
                if data != None :
                     request.session['pId'] = "admin"
                     request.session['userData'] = models.select_loginuser_data(data[0])
                     return redirect("baseapp:admin_dashboard")
          else :                
            data = models.select_login_data(contact,password)
          if data != None :                
            request.session['pId'] = data[0]
            request.session['userData'] = models.select_loginuser_data(data[0])
            request.session['contact'] = data[3]
            if data[2] == 2 :
                  return redirect("common:pending_card")
            if data[1] == 1 :
                  return redirect("patient:dashboard")
            elif data[1] == 2 :
                  return redirect("psychiatrist:dashboard")
            elif data[1] == 3 :
                  return redirect("psychologist:dashboard")
          else :
               data = models.select_organizationlogin_data(contact,password)
               if data != None :
                    request.session['pId'] = data[0]
                    request.session['userData'] = models.select_loginuser_data(data[0])
                    return redirect("organization:dashboard")
               else :
                    data = models.select_diagnosislogin_data(contact,password)
                    if data != None :
                        request.session['pId'] = data[0]
                        request.session['userData'] = models.select_loginuser_data(data[0])
                        return redirect("diagnosis:dashboard")
    return render(request, "registration/login.html")

def signup(request) :    
    if request.method == 'POST': 
        account_type = request.POST.get('accountType', '')        
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        account_type = request.POST.get('accountType', '')
        gender = request.POST.get('gender', '')
        dob = request.POST.get('dob', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        request.session['contact'] = contact
        blood_group = request.POST.get('blood', '')            
        country = request.POST.get('country', '')
        password = request.POST.get('password', '')
        cpassword = request.POST.get('cpassword', '')
      #   img = request.FILE.get('profileImg', '')
        img = "later"
        arr = (fname,lname,gender,contact,email,dob,blood_group,country,password,img,account_type)
        if account_type == "1" :
                patient.models.insert_data(arr)
                print(arr)
        elif account_type == "2" :
                psychiatrist.models.insert_data(arr)
                print(arr)
        elif account_type == "3" :
                psychologist.models.insert_data(arr)
                print(arr)
        return redirect("common:pending_card")
    return render(request, "registration/signup.html")