from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Mufredat
from .models import Kullanicilar, DefaultDegerler, KURANIKERIM, SiyeriNebi, YasinSuresi, MulkSuresi, NebeSuresi, Tecvid, \
    FilSuresiNasSuresiArasi, AlakBeyyineSureleri, DuhaSuresiHumezeSuresiArasi, KullaniciHesaplari
from django.contrib.auth.models import User
from django.contrib import messages, auth
import pandas as pd

# Verification

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import FormView
from randomapp.forms import CustomUserCreationForm
from .tokens import account_activate_token

KURANIKERIM_max = 600
KURANIKERIM_min = 0


class RegisterUser(SuccessMessageMixin, FormView):
    form_class = CustomUserCreationForm
    template_name = 'index/register.html'
    success_url = reverse_lazy('index')
    success_message = 'Başarıyla kayıt oldunuz! Ancak giriş yapmadan önce hesabınızı etkinleştirin!'

    def form_valid(self, form):
        user = form.save(commit=False)
        if KullaniciHesaplari.objects.filter(email=user.email):
            user.save()
            hesap = KullaniciHesaplari.objects.filter(email=user.email).last()
            main_user = User.objects.get(email=hesap.email)
            main_user.set_password(hesap.sifre)
            main_user.save()

        mail_subject = 'Mail adresinize gelen aktivasyon linkine tıklayın daha sonra giriş yapın.'
        current_site = get_current_site(self.request)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activate_token.make_token(user)
        link_dict = {'url': reverse('activate', kwargs={'uidb64': uid, 'token': token})}
        link = f"{get_current_site(self.request).domain}{link_dict.get('url')}"
        message = render_to_string('index/activate_account.html', {
            'user': user, 'domain': current_site.domain,
            'uid': uid, 'token': token
        })
        print(user.email)
        if KullaniciHesaplari.objects.filter(email=user.email):
            email = send_mail(mail_subject, message, settings.EMAIL_HOST_USER, (user.email,),
                              fail_silently=True)
            print('success\n', link) if email else print('ters giden bir şeyler var!')
        else:
            print('success')
        return super().form_valid(form)


class LoginUserView(SuccessMessageMixin, LoginView):
    template_name = 'index/login.html'
    form_class = AuthenticationForm
    success_message = 'Başarıyla giriş yaptınız '


class ActivateView(View):

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, TypeError, ValueError, OverflowError):
            user = None
        if user is not None and account_activate_token.check_token(user=user, token=token):
            user.is_active = True
            user.save()
            login(request=request, user=user)
            messages.add_message(request, messages.INFO, 'Hesabınız başarıyla aktifleştirildi.')
            return redirect('index')
        else:
            return HttpResponse('The link is invalid sorry!')


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
        context['AlakBeyyineSureleri_random'] = AlakBeyyineSureleri.objects.order_by('?')[0]
    elif randomsoru == 6:
        context['DuhaSuresininAlti_random'] = DuhaSuresiHumezeSuresiArasi.objects.order_by('?')[0]
    elif randomsoru == 7:
        context['FilSuresininAlti_random'] = FilSuresiNasSuresiArasi.objects.order_by('?')[0]
    elif randomsoru == 8:
        context['Tecvid_random'] = Tecvid.objects.order_by('?')[0].soru
    elif randomsoru == 9:
        context['SiyeriNebi_random'] = SiyeriNebi.objects.order_by('?')[0]
    elif randomsoru == 10:
        return  # p_arapca
    elif randomsoru == 11:
        if request.POST:
            if request.user.is_authenticated:
                kullanici = Kullanicilar.objects.filter(user=request.user).last()
                if request.POST['KURANIKERIM_b'] and request.POST['KURANIKERIM_s']:
                    if str(request.POST['KURANIKERIM_s']).isdigit() and str(request.POST['KURANIKERIM_b']).isdigit():
                        if (int(request.POST['KURANIKERIM_b']) > int(request.POST['KURANIKERIM_s'])) or (
                                int(request.POST['KURANIKERIM_b']) < KURANIKERIM_min or int(
                            request.POST['KURANIKERIM_s']) > KURANIKERIM_max):
                            context['KURANIKERIM_b'] = KURANIKERIM_min
                            context['KURANIKERIM_s'] = KURANIKERIM_max
                        else:
                            context['KURANIKERIM_b'] = request.POST['KURANIKERIM_b']
                            context['KURANIKERIM_s'] = request.POST['KURANIKERIM_s']
                    else:
                        context['KURANIKERIM_b'] = KURANIKERIM_min
                        context['KURANIKERIM_s'] = KURANIKERIM_max
                else:
                    if kullanici:
                        context['KURANIKERIM_b'] = kullanici.KURANIKERIMSayfaIlk
                        context['KURANIKERIM_s'] = kullanici.KURANIKERIMSayfaSon
                    else:
                        context['KURANIKERIM_b'] = KURANIKERIM_min
                        context['KURANIKERIM_s'] = KURANIKERIM_max
            else:
                if request.POST['KURANIKERIM_b'] and request.POST['KURANIKERIM_s']:
                    if type(request.POST['KURANIKERIM_s']) == int or type(request.POST['KURANIKERIM_b']) == int:
                        if (int(request.POST['KURANIKERIM_b']) > int(request.POST['KURANIKERIM_s'])) or (
                                int(request.POST['KURANIKERIM_b']) < KURANIKERIM_min or int(
                            request.POST['KURANIKERIM_s']) > KURANIKERIM_max):
                            context['KURANIKERIM_b'] = KURANIKERIM_min
                            context['KURANIKERIM_s'] = KURANIKERIM_max
                    else:
                        context['KURANIKERIM_b'] = KURANIKERIM_min
                        context['KURANIKERIM_s'] = KURANIKERIM_max
                else:
                    context['KURANIKERIM_b'] = KURANIKERIM_min
                    context['KURANIKERIM_s'] = KURANIKERIM_max
            print(context['KURANIKERIM_b'], context['KURANIKERIM_s'])
            context['KURANIKERIM_random'] = \
                KURANIKERIM.objects.filter(sayfa__range=(context['KURANIKERIM_b'], context['KURANIKERIM_s'])).order_by(
                    '?')[
                    0]
            context['KURANIKERIM_random'].ayet_no = str(context['KURANIKERIM_random'].ayet_no).replace('1',
                                                                                                       '١').replace('2',
                                                                                                                    '٢').replace(
                '3',
                '٣').replace(
                '4', '٤').replace('5', '٥').replace('6', '٦').replace('7', '٧').replace('8', '٨').replace('9',
                                                                                                          '٩').replace(
                '0', '.')
            context['KURANIKERIM_random'].sayfa = str(context['KURANIKERIM_random'].sayfa).replace('1', '١').replace(
                '2',
                '٢').replace('3',
                             '٣').replace(
                '4', '٤').replace('5', '٥').replace('6', '٦').replace('7', '٧').replace('8', '٨').replace('9',
                                                                                                          '٩').replace(
                '0', '۰')
            return render(request, 'index/index.html', context)
    else:
        if request.user.is_authenticated:
            if Kullanicilar.objects.filter(user=request.user):
                kullanici = Kullanicilar.objects.filter(user=request.user).last()
                if kullanici.KURANIKERIMSayfaIlk and kullanici.KURANIKERIMSayfaSon:
                    context['KURANIKERIM_b'] = kullanici.KURANIKERIMSayfaIlk
                    context['KURANIKERIM_s'] = kullanici.KURANIKERIMSayfaSon
            else:
                context['KURANIKERIM_b'] = KURANIKERIM_min
                context['KURANIKERIM_s'] = KURANIKERIM_max

    return render(request, 'index/index.html', context)


@login_required
def mufredat(request):
    gecmis_mufredat = Kullanicilar.objects.filter(user=request.user).last()
    if request.method == 'POST':
        form = Mufredat(request.POST, instance=gecmis_mufredat)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('mufredat')
    else:
        form = Mufredat(instance=gecmis_mufredat)
    return render(request, 'index/mufredat.html', {'form': form})


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

'''
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
                    user.is_active = False
                    user.save()

                    # Kullanicilar.objects.create(user=user, session=request.session.session_key)
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
'''
"""

    :param request: 
    :param randomsoru: 
    :return: 

    # .xlsx Veri Çekme
    dfs = pd.read_excel("1-Cem'i Kuran (Ezber Yerleri Hariç).xlsx", sheet_name='Veri')
    i = 0
    while i < 5556:
        print(dfs.values[i][0])
        print(dfs.values[i][1])
        print(dfs.values[i][2])
        print(dfs.values[i][3])
        KURANIKERIM.objects.create(sure_isim=dfs.values[i][0],sayfa=dfs.values[i][1],ayet_no=dfs.values[i][2],ayet=dfs.values[i][3])
        i += 1
    """
