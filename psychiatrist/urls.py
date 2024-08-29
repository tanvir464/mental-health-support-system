from django.urls import path
from . import views

app_name = "psychiatrist"
urlpatterns = [
    path('',views.index, name="dashboard"),
    path('list/', views.psychiatrist_list, name="psychiatrist_list"),
    path('appointments/', views.appointments, name="appointments"),
    path('card/<int:id>', views.psychiatrist_card, name="card"),
]