from django.shortcuts import render, redirect
from .forms import Mufredat
from .models import Kullanicilar, DefaultDegerler, KURANIKERIM, siyer


def index(request, randomsoru=0):
    context = dict()
    context['default_degerler'] = DefaultDegerler.objects.last()
    if randomsoru == 1:
        context['yasin_random'] = KURANIKERIM.objects.filter(sure_isim='يٰسۤ').order_by('?')[0].ayet
        context['sure_isim'] = 'يٰسۤ'
    elif randomsoru == 2:
        return  # mulk
    elif randomsoru == 3:
        return  # nebe
    elif randomsoru == 4:
        return  # igra
    elif randomsoru == 5:
        return  # beyyine
    elif randomsoru == 6:
        return  # duha_alti
    elif randomsoru == 7:
        return  # fil_alti
    elif randomsoru == 8:
        return  # tecvid
    elif randomsoru == 9:
        
        context['siyer_random'] = siyer.objects.order_by('?')[0]
    elif randomsoru == 10:
        return  # p_arapca
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


def randomsoru(request, randomsoru):
    context = dict()
    if randomsoru == 1:
        context['yasin_random'] = KURANIKERIM.objects.filter(sure_isim='يٰسۤ').order_by('?')[0].ayet
        context['sure_isim'] = 'يٰسۤ'
    elif randomsoru == 2:
        return  # mulk
    elif randomsoru == 3:
        return  # nebe
    elif randomsoru == 4:
        return  # igra
    elif randomsoru == 5:
        return  # beyyine
    elif randomsoru == 6:
        return  # duha_alti
    elif randomsoru == 7:
        return  # fil_alti
    elif randomsoru == 8:
        return  # tecvid
    elif randomsoru == 9:
        return  # siyer
    elif randomsoru == 10:
        return  # p_arapca

    return redirect(request, 'index/random.html', context)
