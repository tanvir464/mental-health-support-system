from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from . import models 
from common import models as common_models
from baseapp import models as base_models
from diagnosis import models as diag_models
from registration import models as register_models
from . import open_ai
from datetime import datetime
# import datetime


# Create your views here.
def index(request):
    id = request.session.get("pId", '')
    data = models.select_user_data(id)
    apdata = models.select_appointment_data(id)
    app = len(apdata)
    appdata = []
    for d in apdata :
        if d[3] == datetime.today().date() :
            appdata.append(d)
    ev = common_models.select_event_data(id)
    cnt = [0,0]
    event=[]
    for e in ev :
        if e[6] == datetime.today().date() :
            event.append(d)
        if e[4] == 1 :
            cnt[0] += 1
        elif e[4] == 2 :
            cnt[1] += 1    
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
        'app' : app ,
        'appointment' : appdata ,
        'wish' : wish ,
        'cnt' : cnt,
        'event' : event,
    }
    return render(request, "patient/patient_dashboard.html", context)

def appointment(request):
    id = request.session.get("pId",'')
    if id == "admin" :
        data = base_models.select_patientappointment_data()
        center = base_models.select_centerappointmentpatient_data()
    else :
        data = models.select_appointment_data(id)
        center = diag_models.select_appointmentpatient_data(id)
    context = {
        'userId' : id,
        'data' : data,
        "center" : center
    }
    print(context)
    # Data
    return render(request, "patient/appointment.html", context)

def newappointment(request):    
    if request.method == 'POST':
        spId = request.POST.get('specialistNameId', '')
        ppId = request.session.get('pId', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        arr = (ppId,spId,date,time)
        print(arr)
        models.insert_appointment_data(arr)
    data = models.select_readforappointment_data()
    return render(request, "patient/createAppointment.html", {"data" : data})

def patient_resources(request):
    return render(request, "patient/resources.html")

def health_records(request):
    id = request.session.get('pId', '')
    if id == "admin" :
        presdata = base_models.select_patientprescription_data()
        reportdata = base_models.select_patientreport_data()
    else :
        presdata = models.select_prescription_data(id)
        reportdata = models.select_report_data(id)
    print(reportdata)
    context = {
        'presdata' : presdata,
        'reportdata' : reportdata,
    }
    return render(request, "patient/health_records.html", context)

def patient_list(request):
    user = request.session.get("pId" , "")
    testdata = request.session.get("userData" , "")
    print(testdata)

    data = models.select_data()
    context = {
        "user" : user,
        "data" : data,
    }
    return render(request, "patient/patient_list.html" , context)

def pending_patient_list(request):
    data = models.select_pending_data()
    context = {
        "data" : data,
    }
    if request.method == "POST" :
        action = request.POST.get("action", '')
        c = request.POST.get("c", '')
        if c == "acceptbutton" :
            base_models.update_pendinguser_data(action)
        return JsonResponse({'status': 'success'})
    return render(request, "patient/pending_patient.html" , context)

def patient_card(request, id):
    data = models.select_patientcard_data(id)
    presdata = models.select_prescription_data(id)
    reportdata = models.select_report_data(id)
    event = common_models.select_event_data(id)
    context = {
        'data' : data,
        'presdata' : presdata,
        'reportdata' : reportdata,
        'event' : event
    }
    return render(request, "patient/patient_card.html", context)

def prescription(request, id):
    data,patient,specialist,fee = common_models.select_appointmentcard_data(id)
    context = {
        "data" : data ,
        "patient" : patient,
        "specialist" : specialist,
        "today" : datetime.now().strftime("%Y-%m-%d"),
    }
    if request.method == "POST" :
        test = request.POST.get("test", '')
        medicine = request.POST.get("medicine", '')
        advice = request.POST.get("advice", '')
        arr = (id,test,medicine,advice,context['today'])
        models.insert_prescription_data(arr)
        print(arr)
        # return redirect(f"patient:appointment_card/{id}")
    return render(request, "patient/prescription.html", context)

def prescription_card(request,id) :
    user = register_models.select_loginuser_data(request.session.get('pId',''))
    pres,spe,patient = models.select_prescriptioncard_data(id)
    pres = list(pres)
    test = pres[2].split("\r\n")
    medicine = pres[3].split("\r\n")
    advice = pres[4].split("\r\n")
    dob = patient[4].year
    today = datetime.today().date().year
    age = today - dob
    context = {
        "user" : user,
        "pres" : pres,
        "spe" : spe,
        "patient" : patient,
        "test" : test,
        "medicine" : medicine,
        "advice" : advice,
        "age" : age,
    }
    return render(request, "patient/prescription_card.html",context)

def report(request):
    return render(request, "patient/report.html")

def recommandation(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input')
        response = open_ai.get_chatgpt_response(user_input)
        return JsonResponse(response)
    return render(request, "patient/patient_recommandation.html")

def profile(request):
    id = request.session.get('pId', '')
    data = models.select_profile_data(id)
    if request.method == "POST" :
        fname = request.POST.get("fname", '')
        lname = request.POST.get("lname", '')
        img = request.POST.get("profileImg", '')
        house = request.POST.get("house", '')
        road = request.POST.get("road", '')
        area = request.POST.get("area", '')
        district = request.POST.get("district", '')
        country = request.POST.get("country", '')
        education = request.POST.get("education", '')
        employment = request.POST.get("employment", '')
        password = request.POST.get("password", '')
        arr = (fname,lname,img,house,road,area,district,country,education,employment,password,id)
        base_models.update_patientprofile_data(arr)        

    return render(request, "patient/patient_profile.html",{'data' : data})

def get_chart_data(request):
    # Manually define the data as a list of tuples
    rdatas = models.appointment_chart_data()
    data = []

    for datax in rdatas:
        data.append(datax)

    # Process the data to extract counts per month
    specialist_data = [0] * 12
    counselor_data = [0] * 12

    for record in data:
        _, date, _, _, type_id = record
        month_index = date.month - 1  # Convert month to zero-based index

        if type_id == 2:  # Assuming 2 is for Specialist
            specialist_data[month_index] += 1
        elif type_id == 3:  # Assuming 3 is for Counselor
            counselor_data[month_index] += 1

    # Prepare data for JSON response
    chart_data = {
        "series": [
            {
                "name": "Psychiatrist",
                "data": specialist_data,
            },
            {
                "name": "Psychologist",
                "data": counselor_data,
            },
        ],
        "categories": [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ],  # X-axis categories for each month
    }

    return JsonResponse(chart_data)
    # return HttpResponse(chart_data)

def radial_chart(request):
    rdata = [0, 0]
    radial_datas = models.appointment_chart_data()
    for radial_data in radial_datas:
        if radial_data[-1] == 2:
            rdata[0] += 1
        if radial_data[-1] == 3:
            rdata[1] += 1
    
    context = {'radial_data': rdata}
    return JsonResponse(context)

def user_feedback(request):
    return render(request, "patient/feedback.html")