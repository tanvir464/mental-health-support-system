from django.urls import path
from . import views

app_name = "patient"
urlpatterns = [
    path('',views.index, name="dashboard"),
    path("appointment/", views.appointment, name="appointment"),
    path("new_appointment/", views.newappointment, name="new_appointment"),
    path("resources/", views.patient_resources, name="resources"),
    path("records/", views.health_records, name="records"),    
    path("list/", views.patient_list, name="list"),
    path("pending/", views.pending_patient_list, name="pending"),
    path("card/<int:id>", views.patient_card, name="card"),
    path("prescription/<int:id>", views.prescription, name="prescription"),
    path("prescription_card/<int:id>", views.prescription_card, name="prescription_card"),
    path("report/", views.report, name="report"),
    path("recommandation/", views.recommandation, name="recommandation"),
    path("profile/", views.profile, name="profile"),
    path("appointment_chart/", views.get_chart_data, name="appointment_chart"),
    path("radial_chart/", views.radial_chart, name="radial"),
    path("feedback/", views.user_feedback, name="feedback"),
]