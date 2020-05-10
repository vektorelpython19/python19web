from django.shortcuts import render,redirect
from .models import BlogGonderi
from .forms import GonderiForm

def gonderi_list(request):
    gonderiler = BlogGonderi.objects.all()
    return render(request,'Blog/gonderilist.html',{"gonderiler":gonderiler})

def gonderi_detay(request,pk):
    gonderi = BlogGonderi.objects.get(pk=pk)
    return render(request,'Blog/gonderidetay.html',{"gonderi":gonderi})

def gonderi_duzenle(request):
    if request.method == "POST":
        form = GonderiForm(request.POST)
        if form.is_valid():
            gonderi = form.save(commit=False)
            # işlemler yapabilirsiniz
            gonderi.save()
            return redirect('detaygon',pk=gonderi.pk)
    else:
        form = GonderiForm()
    return render(request,'Blog/yenigonderi.html',{"form":form})