from django.contrib import admin
from .views import Kullanicilar,DefaultDegerler
from .models import siyer
admin.site.register(Kullanicilar)
admin.site.register(DefaultDegerler)
admin.site.register(siyer)
# Register your models here.
