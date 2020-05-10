from django.urls import path
from  . import views
urlspatterns = [
    path('',views.gonderi_list,name="listgonderi")
]