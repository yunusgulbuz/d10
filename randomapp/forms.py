from django import forms
from django.core.exceptions import ValidationError

from randomapp.models import Kullanicilar
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = [
            'username', 'email', 'password1', 'password2'
        ]

    def clean_email(self):
        if UserModel.objects.filter(email=self.cleaned_data.get('email')).exists():
            raise forms.ValidationError('Bu mail sisteme kayıtlı')
        return self.cleaned_data['email']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.email = self.cleaned_data.get('email')
            user.is_active = False
            user.save()
        return user


class Mufredat(forms.ModelForm):
    KURANIKERIMSayfaIlk = forms.IntegerField(label="Kur'an-ı Kerim başlangıç", max_value=600, min_value=0)
    KURANIKERIMSayfaSon = forms.IntegerField(label="Kur'an-ı Kerim bitiş", max_value=600, min_value=0)
    IlmihalIlk = forms.IntegerField(label="İlmihal başlangıç", max_value=238, min_value=0)
    IlmihalSon = forms.IntegerField(label="İlmihal başlangıç", max_value=238, min_value=0)

    def clean(self):
        data1 = self.cleaned_data['KURANIKERIMSayfaIlk']
        data2 = self.cleaned_data['KURANIKERIMSayfaSon']
        data3 = self.cleaned_data['IlmihalIlk']
        data4 = self.cleaned_data['IlmihalSon']
        if (data1 > data2) or (data3 > data4):
            raise ValidationError("Başlangıç sayfası bitiş sayfasından büyük olamaz.")

    class Meta:
        model = Kullanicilar
        fields = [
            'KURANIKERIMSayfaIlk',
            'KURANIKERIMSayfaSon',
            'IlmihalIlk',
            'IlmihalSon',
            'YasinSuresi',
            'MulkSuresi',
            'NebeSuresi',
            'AlakSuresi',
            'BeyyineSuresi',
            'DuhaSuresininAlti',
            'FilSuresininAlti',
            'Tecvid',
            'SiyeriNebi',
            'PratikArapca',

        ]
        labels = {
            'KURANIKERIMSayfaIlk': "Kur'an-ı Kerim sayfası başlangıç",
            'KURANIKERIMSayfaSon': "Kur'an-ı Kerim sayfası bitiş",
            'IlmihalIlk': 'İlmihal sayfası başlangıç',
            'IlmihalSon': 'İlmihal sayfası son',
            'YasinSuresi': 'Yasin Suresi',
            'MulkSuresi': 'Mülk Suresi',
            'NebeSuresi': 'Nebe Suresi',
            'AlakSuresi': 'İgra Suresi',
            'BeyyineSuresi': 'Beyyine Suresi',
            'DuhaSuresininAlti': "Duha Suresi'nin Alt Kısmı",
            'FilSuresininAlti': "Fil Suresi'nin Alt Kısmı",
            'Tecvid': 'Tecvid Sualleri',
            'SiyeriNebi': 'Siyer Sualleri',
            'PratikArapca': 'Pratik Arapça Sualleri',

        }
        widgets = {
            'KURANIKERIMSayfaIlk': forms.TextInput(attrs={'class': 'input', 'placeholder': '40'}),
            'KURANIKERIMSayfaSon': forms.TextInput(attrs={'class': 'input', 'placeholder': '120'}),
            'IlmihalIlk': forms.TextInput(attrs={'class': 'input', 'placeholder': '0'}),
            'IlmihalSon': forms.TextInput(attrs={'class': 'input', 'placeholder': '50'}),
        }
