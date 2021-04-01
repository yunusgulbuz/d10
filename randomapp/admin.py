from django.contrib import admin
from .models import Kullanicilar, DefaultDegerler, KURANIKERIM, Tecvid, KullaniciHesaplari
from .models import SiyeriNebi, FilSuresiNasSuresiArasi, AlakBeyyineSureleri, DuhaSuresiHumezeSuresiArasi

admin.site.register(Kullanicilar)
admin.site.register(DefaultDegerler)
admin.site.register(SiyeriNebi)
admin.site.register(KURANIKERIM)
admin.site.register(Tecvid)
admin.site.register(FilSuresiNasSuresiArasi)
admin.site.register(AlakBeyyineSureleri)
admin.site.register(DuhaSuresiHumezeSuresiArasi)
admin.site.register(KullaniciHesaplari)
# Register your models here.
