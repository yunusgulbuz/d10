
from django import forms

from randomapp.models import Kullanicilar

'''
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
'''

'''
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
'''

class Mufredat(forms.ModelForm):
    class Meta:
        model = Kullanicilar
        fields = [
            'kk_sayfa_ilk',
            'kk_sayfa_son',
            'ilmihal_ilk',
            'ilmihal_son',



        ]
        labels = {
            'kk_sayfa_ilk': "Kur'an-ı Kerim sayfası başlangıç",
            'kk_sayfa_son': "Kur'an-ı Kerim sayfası bitiş",
            'ilmihal_ilk': 'İlmihal sayfası başlangıç',
            'ilmihal_son': 'İlmihal sayfası son'


        }
        widgets = {
            'kk_sayfa_ilk': forms.TextInput(attrs={'class': 'input', 'placeholder': '40'}),
            'kk_sayfa_son': forms.TextInput(attrs={'class': 'input', 'placeholder': '120'}),
            'ilmihal_ilk': forms.TextInput(attrs={'class': 'input', 'placeholder': '0'}),
            'ilmihal_son': forms.TextInput(attrs={'class': 'input', 'placeholder': '50'}),
        }
