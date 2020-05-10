from django.shortcuts import render,redirect,get_object_or_404
from .models import BlogGonderi
from .forms import GonderiForm

def gonderi_list(request):
    gonderiler = BlogGonderi.objects.filter(yazar=request.user)
    return render(request,'Blog/gonderilist.html',{"gonderiler":gonderiler})

def gonderi_detay(request,pk):
    gonderi = BlogGonderi.objects.get(pk=pk)
    return render(request,'Blog/gonderidetay.html',{"gonderi":gonderi})

def gonderi_ekle(request):
    if request.method == "POST":
        form = GonderiForm(request.POST)
        if form.is_valid():
            gonderi = form.save(commit=False)
            gonderi.yazar = request.user
            gonderi.save()
            return redirect('detaygon',pk=gonderi.pk)
    else:
        form = GonderiForm()
    return render(request,'Blog/yenigonderi.html',{"form":form})

def gonderi_duzenle(request,pk):
    gonderi = get_object_or_404(BlogGonderi,pk=pk)
    if request.method == "POST":
        form = GonderiForm(request.POST,instance=gonderi)
        if form.is_valid():
            gonderi = form.save(commit=False)
            gonderi.yazar = request.user
            gonderi.save()
            return redirect('detaygon',pk=gonderi.pk)
    else:
        form = GonderiForm(instance=gonderi)
    return render(request,'Blog/yenigonderi.html',{"form":form})
