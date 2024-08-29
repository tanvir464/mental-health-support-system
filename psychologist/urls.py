from django.urls import path
from . import views

app_name = "psychologist"
urlpatterns = [
    path('',views.index, name="dashboard"),
    path('list/',views.psychologist_list, name="psychologist_list"),
    path('appointments/',views.appointments, name="appointments"),
    path('card/<int:id>',views.psychologist_card, name="card"),
]