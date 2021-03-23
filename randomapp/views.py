from django.shortcuts import render, redirect
from .forms import Mufredat
from .models import Kullanicilar, DefaultDegerler, KURANIKERIM
import pandas as pd


def index(request):
    file_name = './ayetler.xlsx'
    context = dict()
    #dfs = pd.read_excel(file_name, sheet_name='Veri')
    i = 2
    j = 0
    # while i < 6236:
    #    kk = KURANIKERIM(sure_isim=dfs['sure_isim'][i], sayfa=dfs['sayfa'][i], ayet_no=dfs['ayet_no'][i],
    #                     ayet=dfs['ayet'][i])
    #    kk.save()
    #    i += 1

    context['default_degerler'] = DefaultDegerler.objects.last()

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
    if randomsoru == 1:
        return print('Yasin Suresi')  # yasin
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

    return render(request, 'index/index.html')
