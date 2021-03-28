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
    kk_sayfa_ilk = forms.IntegerField(label="Kur'an-ı Kerim başlangıç", max_value=600, min_value=0)
    kk_sayfa_son = forms.IntegerField(label="Kur'an-ı Kerim bitiş", max_value=600, min_value=0)
    ilmihal_ilk = forms.IntegerField(label="İlmihal başlangıç", max_value=238, min_value=0)
    ilmihal_son = forms.IntegerField(label="İlmihal başlangıç", max_value=238, min_value=0)

    def clean(self):
        data1 = self.cleaned_data['kk_sayfa_ilk']
        data2 = self.cleaned_data['kk_sayfa_son']
        data3 = self.cleaned_data['ilmihal_ilk']
        data4 = self.cleaned_data['ilmihal_son']
        if (data1 > data2) or (data3 > data4):
            raise ValidationError("Başlangıç sayfası bitiş sayfasından büyük olamaz.")

    class Meta:
        model = Kullanicilar
        fields = [
            'kk_sayfa_ilk',
            'kk_sayfa_son',
            'ilmihal_ilk',
            'ilmihal_son',
            'yasin',
            'mulk',
            'nebe',
            'igra',
            'beyyine',
            'duha_alti',
            'fil_alti',
            'tecvid',
            'siyer',
            'p_arapca',

        ]
        labels = {
            'kk_sayfa_ilk': "Kur'an-ı Kerim sayfası başlangıç",
            'kk_sayfa_son': "Kur'an-ı Kerim sayfası bitiş",
            'ilmihal_ilk': 'İlmihal sayfası başlangıç',
            'ilmihal_son': 'İlmihal sayfası son',
            'yasin': 'Yasin Suresi',
            'mulk': 'Mülk Suresi',
            'nebe': 'Nebe Suresi',
            'igra': 'İgra Suresi',
            'beyyine': 'Beyyine Suresi',
            'duha_alti': "Duha Suresi'nin Alt Kısmı",
            'fil_alti': "Fil Suresi'nin Alt Kısmı",
            'tecvid': 'Tecvid Sualleri',
            'siyer': 'Siyer Sualleri',
            'p_arapca': 'Pratik Arapça Sualleri',

        }
        widgets = {
            'kk_sayfa_ilk': forms.TextInput(attrs={'class': 'input', 'placeholder': '40'}),
            'kk_sayfa_son': forms.TextInput(attrs={'class': 'input', 'placeholder': '120'}),
            'ilmihal_ilk': forms.TextInput(attrs={'class': 'input', 'placeholder': '0'}),
            'ilmihal_son': forms.TextInput(attrs={'class': 'input', 'placeholder': '50'}),
        }
