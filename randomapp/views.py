from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Mufredat
from .models import Kullanicilar, DefaultDegerler, KURANIKERIM, siyer, YasinSuresi, MulkSuresi, NebeSuresi
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

KK_max = 600
KK_min = 0


class RegisterUser(SuccessMessageMixin, FormView):
    form_class = CustomUserCreationForm
    template_name = 'index/register.html'
    success_url = reverse_lazy('index')
    success_message = 'Başarıyla kayıt oldunuz! Ancak giriş yapmadan önce hesabınızı etkinleştirin!'

    def form_valid(self, form):
        user = form.save(commit=True)

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
        email = send_mail(mail_subject, message, settings.EMAIL_HOST_USER, (user.email,),
                          fail_silently=True)
        print('success\n', link) if email else print('ters giden bir şeyler var!')
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
        if request.POST:
            if request.user.is_authenticated:
                kullanici = Kullanicilar.objects.filter(user=request.user).last()
                if request.POST['kk_b'] and request.POST['kk_s']:
                    if str(request.POST['kk_s']).isdigit() and str(request.POST['kk_b']).isdigit():
                        if (int(request.POST['kk_b']) > int(request.POST['kk_s'])) or (
                                int(request.POST['kk_b']) < KK_min or int(request.POST['kk_s']) > KK_max):
                            context['kk_b'] = KK_min
                            context['kk_s'] = KK_max
                        else:
                            context['kk_b'] = request.POST['kk_b']
                            context['kk_s'] = request.POST['kk_s']
                    else:
                        context['kk_b'] = KK_min
                        context['kk_s'] = KK_max
                else:
                    if kullanici:
                        context['kk_b'] = kullanici.kk_sayfa_ilk
                        context['kk_s'] = kullanici.kk_sayfa_son
                    else:
                        context['kk_b'] = KK_min
                        context['kk_s'] = KK_max
            else:
                if request.POST['kk_b'] and request.POST['kk_s']:
                    if type(request.POST['kk_s']) == int or type(request.POST['kk_b']) == int:
                        if (int(request.POST['kk_b']) > int(request.POST['kk_s'])) or (
                                int(request.POST['kk_b']) < KK_min or int(request.POST['kk_s']) > KK_max):
                            context['kk_b'] = KK_min
                            context['kk_s'] = KK_max
                    else:
                        context['kk_b'] = KK_min
                        context['kk_s'] = KK_max
                else:
                    context['kk_b'] = KK_min
                    context['kk_s'] = KK_max

            context['kk_random'] = \
                KURANIKERIM.objects.filter(sayfa__range=(context['kk_b'], context['kk_s'])).order_by('?')[
                    0]
            context['kk_random'].ayet_no = str(context['kk_random'].ayet_no).replace('1', '١').replace('2',
                                                                                                       '٢').replace('3',
                                                                                                                    '٣').replace(
                '4', '٤').replace('5', '٥').replace('6', '٦').replace('7', '٧').replace('8', '٨').replace('9',
                                                                                                          '٩').replace(
                '0', '.')
            context['kk_random'].sayfa = str(context['kk_random'].sayfa).replace('1', '١').replace('2',
                                                                                                   '٢').replace('3',
                                                                                                                '٣').replace(
                '4', '٤').replace('5', '٥').replace('6', '٦').replace('7', '٧').replace('8', '٨').replace('9',
                                                                                                          '٩').replace(
                '0', '.')
            return render(request, 'index/index.html', context)
    else:
        if request.user.is_authenticated:
            if Kullanicilar.objects.filter(user=request.user):
                kullanici = Kullanicilar.objects.filter(user=request.user).last()
                if kullanici.kk_sayfa_ilk and kullanici.kk_sayfa_son:
                    context['kk_b'] = kullanici.kk_sayfa_ilk
                    context['kk_s'] = kullanici.kk_sayfa_son
            else:
                context['kk_b'] = KK_min
                context['kk_s'] = KK_max

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
    gecmis_mufredat = Kullanicilar.objects.filter(user=request.user).last()
    if request.method == 'POST':
        form = Mufredat(request.POST, instance=gecmis_mufredat)
        if form.is_valid():
            item = form.save(commit=False)
            item.kk_sayfa_ilk
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
