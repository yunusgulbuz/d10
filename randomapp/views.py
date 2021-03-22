from django.shortcuts import render, redirect
from .forms import Mufredat
from .models import Kullanicilar


def index(request):
    context = dict()
    session = request.session.session_key
    if request.method == 'POST':
        form = Mufredat(request.POST)
        if form.is_valid():
            mufredat = form.save(commit=False)
            mufredat.session = session
            mufredat.save()
            return redirect('index')
    else:
        if Kullanicilar.objects.filter(session=session):
            kullanici = Kullanicilar.objects.filter(session=session).last()
            context['sorular'] = kullanici
        context['form'] = Mufredat()
    return render(request, 'index/index.html', context)
