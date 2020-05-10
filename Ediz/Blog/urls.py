from django.urls import path
from . import views

urlpatterns = [
    path('',views.gonderi_list,name="listgonderi"),
    path('detay/<int:pk>/',views.gonderi_detay,name="detaygon"),
    path('gonderi/yeni/',views.gonderi_ekle,name="yenigon"),
    path('gonderi/duzenle/<int:pk>',views.gonderi_duzenle,name="duzenlegon"),
]
