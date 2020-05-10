from django.urls import path
from .import views
urlpatterns = [
    path('',views.gonderi_list,name="listgonderi"),


]