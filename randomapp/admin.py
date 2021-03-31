from django.contrib import admin
from .models import Kullanicilar, DefaultDegerler, KURANIKERIM
from .models import SiyeriNebi

admin.site.register(Kullanicilar)
admin.site.register(DefaultDegerler)
admin.site.register(SiyeriNebi)
admin.site.register(KURANIKERIM)
# Register your models here.
