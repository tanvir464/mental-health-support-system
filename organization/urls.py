from django.urls import path
from . import views

app_name = "organization"
urlpatterns = [
    path('',views.index, name="dashboard"),
    path('list/',views.list, name="list"),
    path('card/<int:id>/',views.card, name="card"),
    path('add/',views.add, name="add"),
    path('events/', views.events, name="events"),
    path('create/', views.create_events, name="create_event"),
    path('workshop/<int:id>/', views.workshop, name="workshop"),
    path('seminar/<int:id>/', views.seminar, name="seminar"),
    path('event_card/<int:id>/', views.event_card, name="event_card"),
]