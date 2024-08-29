from django.urls import path
from . import views

app_name = "baseapp"
urlpatterns = [
    path('landpage/', views.landpage, name="landpage"),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),    
]