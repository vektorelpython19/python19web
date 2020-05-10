from django.shortcuts import render
from .models import BlogGonderi

def gonderi_list(request):
    gonderiler = BlogGonderi.objects.all()
    return render(request,'Blog/gonderilist.html',{"gonderiler":gonderiler})

