from django.shortcuts import render

# Create your views here.
def landpage(request) :
    return render(request, "baseapp/landpage.html")

def admin_dashboard(request) :
    return render(request, "baseapp/admin_dashboard.html")