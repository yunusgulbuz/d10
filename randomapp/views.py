from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import Mufredat
from .models import Kullanicilar, DefaultDegerler, KURANIKERIM, siyer, YasinSuresi, MulkSuresi, NebeSuresi
from django.contrib.auth.models import User
from django.contrib import messages, auth
import pandas as pd


def index(request, randomsoru=0):
    context = dict()
    context['default_degerler'] = DefaultDegerler.objects.last()
    if randomsoru == 1:
        context['YasinSuresi_random'] = YasinSuresi.objects.order_by('?')[0].soru
    elif randomsoru == 2:
        context['MulkSuresi_random'] = MulkSuresi.objects.order_by('?')[0].soru
    elif randomsoru == 3:
        context['NebeSuresi_random'] = NebeSuresi.objects.order_by('?')[0].soru
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
    elif randomsoru == 11:
        print('deneme')
        if request.POST:
            if request.user.is_authenticated:
                print('geldidiiid')
                print(request.POST['kk_b'], request.POST['kk_s'])
                kullanici = Kullanicilar.objects.get(user__username=auth.get_user(request).username)
                if request.POST['kk_b'] and request.POST['kk_s']:
                    if (int(request.POST['kk_b']) > int(request.POST['kk_s'])) or (
                            int(request.POST['kk_b']) < 0 or int(request.POST['kk_s']) > 600):
                        context['kk_b'] = 1
                        context['kk_s'] = 600
                    else:
                        context['kk_b'] = request.POST['kk_b']
                        context['kk_s'] = request.POST['kk_s']
                else:
                    context['kk_b'] = kullanici.kk_sayfa_ilk
                    context['kk_s'] = kullanici.kk_sayfa_son
            else:
                if request.POST['kk_b'] and request.POST['kk_s']:
                    print('buraya bile geldi')
                    context['kk_b'] = request.POST['kk_b']
                    context['kk_s'] = request.POST['kk_s']
                else:
                    context['kk_b'] = 1
                    context['kk_s'] = 600

            context['kk_random'] = \
                KURANIKERIM.objects.filter(sayfa__range=(context['kk_b'], context['kk_s'])).order_by('?')[
                    0].ayet
            return render(request, 'index/index.html', context)
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
    session = request.session.session_key
    if Kullanicilar.objects.filter(session=session):
        Kullanicilar.objects.get(session=session)
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
    elif randomsoru == 11:
        print('deneme')
        if request.GET:
            if User.is_authenticated:
                print('geldidiiid')
                kullanici = Kullanicilar.objects.get(user=auth.get_user(request))
                if request.POST['kk_b'] and request.GET['kk_s']:
                    context['kk_b'] = request.POST['kk_b']
                    context['kk_s'] = request.POST['kk_s']
                else:
                    context['kk_b'] = kullanici.kk_sayfa_ilk
                    context['kk_s'] = kullanici.kk_sayfa_son
                context['kk_random'] = KURANIKERIM.objects.filter(sayfa_end_int__gte=context['kk_b'],
                                                                  sayfa_begin_int__lte=context['kk_s']).order_by('?')[
                    0].ayet
            else:
                print('gelmediididiid')
                if request.POST['kk_b'] and request.POST['kk_s']:
                    context['kk_b'] = request.POST['kk_b']
                    context['kk_s'] = request.POST['kk_s']
                else:
                    context['kk_b'] = 1
                    context['kk_s'] = 600
                context['kk_random'] = KURANIKERIM.objects.filter(sayfa_end_int__gte=context['kk_b'],
                                                                  sayfa_begin_int__lte=context['kk_s']).order_by('?')[
                    0].ayet
        else:
            print('neden burdayım')
    return redirect(request, 'index/random.html', context)

@login_required
def mufredat(request):
    context = dict()
    context['form'] = Mufredat()
    return render(request, 'index/mufredat.html', context)


def register(request):
    context = dict()
    if request.method == 'POST':
        # get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['sifre']
        repassword = request.POST['resifre']
        if password == repassword:
            # Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Bu kullanıcı adı daha önce alınmış.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Bu email daha önce alınmış.')
                    return redirect('register')
                else:
                    # her şey güzel
                    user = User.objects.create_user(username=username, password=password, email=email, is_active=False)
                    user.save()
                    Kullanicilar.objects.create(user=user, session=request.session.session_key)
                    messages.success(request, 'Hesabınız oluşturuldu.')
                    return redirect('login')
        else:
            messages.error(request, 'Parolalar eşleşmiyor')
            return redirect('register')
    else:
        return render(request, 'index/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['sifre']
        print(password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('girdi')
            messages.success(request, 'Oturum açıldı.')
            return redirect('index')
        else:
            messages.error(request, 'Giriş yapılamadı')
            return redirect('login')
    else:
        return render(request, 'index/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Oturumunuz kapatıldı.')
        return redirect('index')


'''
# .xlsx Veri Çekme
dfs = pd.read_excel('Mulk_Nebe_Sureleri.xlsx', sheet_name='NebeSuresi',header=0)
i = 0
while i < 28:
    print(dfs.values[i][0])
    NebeSuresi_vt = NebeSuresi.objects.create(soru=dfs.values[i][0])
    i += 1
'''
