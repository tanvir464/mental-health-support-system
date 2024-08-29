from django.urls import path
from . import views

app_name = "diagnosis"
urlpatterns = [
    path('',views.index, name="dashboard"),
    path('appointment/',views.appointment, name="appointment"),
    path('add/',views.add, name="add"),
    path('list/',views.list, name="list"),
    path('card/<int:id>/',views.card, name="card"),
    path('make_appointment/<int:id>/',views.make_appointment, name="make_appointment"),
    path('report/<int:id>/',views.report, name="report"),
    path('report_card/<int:id>/',views.report_card, name="report_card"),
]