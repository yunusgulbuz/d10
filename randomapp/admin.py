from django.contrib import admin
from .models import Kullanicilar, DefaultDegerler, KURANIKERIM, Tecvid, KullaniciHesaplari, s_Yasin, s_siyer, s_ilmihal
from .models import SiyeriNebi, FilSuresiNasSuresiArasi, AlakBeyyineSureleri, DuhaSuresiHumezeSuresiArasi, s_tecvid

admin.site.register(Kullanicilar)
admin.site.register(DefaultDegerler)
admin.site.register(SiyeriNebi)
admin.site.register(KURANIKERIM)
admin.site.register(Tecvid)
admin.site.register(FilSuresiNasSuresiArasi)
admin.site.register(AlakBeyyineSureleri)
admin.site.register(DuhaSuresiHumezeSuresiArasi)
admin.site.register(KullaniciHesaplari)
admin.site.register(s_tecvid)
admin.site.register(s_Yasin)
admin.site.register(s_siyer)
admin.site.register(s_ilmihal)
# Register your models here.
