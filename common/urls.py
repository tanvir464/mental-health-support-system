from django.urls import path
from . import views

app_name = "common"
urlpatterns = [
    path('resource/', views.resource, name="resource"),
    path('resource_new/', views.resource_new, name="resource_new"),
    path('resource_card/<int:id>', views.resource_card, name="resource_card"),
    path('event/', views.event, name="event"),
    path("event_/", views.event_, name="event_"),
    path("request_event/", views.request_event, name="request_event"),
    path('event_card/', views.event_card, name="event_card"),
    path('add_doctor/', views.add_doctor, name="add_doctor"),
    path('schedule/', views.schedule, name="schedule"),
    path('appointment_card/<int:id>', views.appointment_card, name="appointment_card"),
    path('pending_card/', views.pending_card, name="pending_card"),
    path('pending_specialist/', views.pending_specialist, name="pending_specialist"),
]