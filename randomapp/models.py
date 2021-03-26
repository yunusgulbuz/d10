from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
MESSAGE_STATUS = (
    ('var', 'Var'),
    ('yok', 'Yok'),
)


class Kullanicilar(models.Model):
    session = models.CharField(blank=True, null=True, max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    yasin = models.CharField(max_length=25,
                             choices=MESSAGE_STATUS,
                             default='var',
                             blank=True,
                             null=True,
                             )
    mulk = models.CharField(max_length=25,
                            choices=MESSAGE_STATUS,
                            default='var',
                            blank=True,
                            null=True,
                            )
    nebe = models.CharField(max_length=25,
                            choices=MESSAGE_STATUS,
                            default='var',
                            blank=True,
                            null=True,
                            )
    igra = models.CharField(max_length=25,
                            choices=MESSAGE_STATUS,
                            default='var',
                            blank=True,
                            null=True,
                            )
    beyyine = models.CharField(max_length=25,
                               choices=MESSAGE_STATUS,
                               default='var',
                               blank=True,
                               null=True,
                               )
    duha_alti = models.CharField(max_length=25,
                                 choices=MESSAGE_STATUS,
                                 default='var',
                                 blank=True,
                                 null=True,
                                 )
    fil_alti = models.CharField(max_length=25,
                                choices=MESSAGE_STATUS,
                                default='var',
                                blank=True,
                                null=True,
                                )
    tecvid = models.CharField(max_length=25,
                              choices=MESSAGE_STATUS,
                              default='var',
                              blank=True,
                              null=True,
                              )
    siyer = models.CharField(max_length=25,
                             choices=MESSAGE_STATUS,
                             default='var',
                             blank=True,
                             null=True,
                             )
    p_arapca = models.CharField(max_length=25,
                                choices=MESSAGE_STATUS,
                                default='var',
                                blank=True,
                                null=True,
                                )
    kk_sayfa_ilk = models.SmallIntegerField("Başlangıç", blank=True, default=1)
    kk_sayfa_son = models.SmallIntegerField("Bitiş", blank=True, default=600)
    ilmihal_ilk = models.SmallIntegerField("Başlangıç", blank=True, default=0)
    ilmihal_son = models.SmallIntegerField("Bitiş", blank=True, default=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.session


class KURANIKERIM(models.Model):
    sure_isim = models.CharField(max_length=100, blank=False)
    sayfa = models.SmallIntegerField()
    ayet_no = models.SmallIntegerField()
    ayet = models.TextField(blank=False)


class ilmihal(models.Model):
    sayfa = models.SmallIntegerField()
    soru = models.TextField(max_length=600, blank=False)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sayfa no : {self.sayfa}"


class siyer(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    sayfa = models.SmallIntegerField(blank=True, default=0)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Siyer soru no : {self.pk}"


class tecvid(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tecvid soru no : {self.pk}"


class PratikArapca(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"P. Arapça soru no : {self.pk}"


class YasinSuresi(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Yasin Suresi soru no : {self.pk}"


class MulkSuresi(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mülk Suresi soru no : {self.pk}"


class NebeSuresi(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mülk Suresi soru no : {self.pk}"


class s_Yasin(models.Model):
    yasin_id = models.ForeignKey(YasinSuresi, blank=False, null=False, on_delete=models.CASCADE)
    kullanici_id = models.ForeignKey(Kullanicilar, blank=False, null=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class s_Mulk(models.Model):
    Mulk_id = models.ForeignKey(MulkSuresi, blank=False, null=False, on_delete=models.CASCADE)
    kullanici_id = models.ForeignKey(Kullanicilar, blank=False, null=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class s_Nebe(models.Model):
    Nebe_id = models.ForeignKey(NebeSuresi, blank=False, null=False, on_delete=models.CASCADE)
    kullanici_id = models.ForeignKey(Kullanicilar, blank=False, null=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class s_ilmihal(models.Model):
    ilmihal_id = models.ForeignKey(ilmihal, blank=False, null=False, on_delete=models.CASCADE)
    kullanici_id = models.ForeignKey(Kullanicilar, blank=False, null=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class s_siyer(models.Model):
    siyer_id = models.ForeignKey(siyer, blank=False, null=False, on_delete=models.CASCADE)
    kullanici_id = models.ForeignKey(Kullanicilar, blank=False, null=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class s_tecvid(models.Model):
    tecvid_id = models.ForeignKey(tecvid, blank=False, null=False, on_delete=models.CASCADE)
    kullanici_id = models.ForeignKey(Kullanicilar, blank=False, null=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class s_parapca(models.Model):
    parapca_id = models.ForeignKey(PratikArapca, blank=False, null=False, on_delete=models.CASCADE)
    kullanici_id = models.ForeignKey(Kullanicilar, blank=False, null=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class s_ezber(models.Model):
    ezber_id = models.ForeignKey(KURANIKERIM, blank=False, null=False, on_delete=models.CASCADE)
    kullanici_id = models.ForeignKey(Kullanicilar, blank=False, null=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class DefaultDegerler(models.Model):
    kk_sayfa_ilk = models.SmallIntegerField("Başlangıç", default=0, blank=True)
    kk_sayfa_son = models.SmallIntegerField("Bitiş", default=604, blank=True)
    ilmihal_ilk = models.SmallIntegerField("Başlangıç", blank=True)
    ilmihal_son = models.SmallIntegerField("Bitiş", blank=True)
    kk = models.CharField(max_length=25,
                          choices=MESSAGE_STATUS,
                          default='var',
                          blank=False,
                          null=False,
                          )

    yasin = models.CharField(max_length=25,
                             choices=MESSAGE_STATUS,
                             default='var',
                             blank=False,
                             null=False,
                             )
    mulk = models.CharField(max_length=25,
                            choices=MESSAGE_STATUS,
                            default='var',
                            blank=False,
                            null=False,
                            )
    nebe = models.CharField(max_length=25,
                            choices=MESSAGE_STATUS,
                            default='var',
                            blank=False,
                            null=False,
                            )
    igra = models.CharField(max_length=25,
                            choices=MESSAGE_STATUS,
                            default='var',
                            blank=False,
                            null=False,
                            )
    beyyine = models.CharField(max_length=25,
                               choices=MESSAGE_STATUS,
                               default='var',
                               blank=False,
                               null=False,
                               )
    duha_alti = models.CharField(max_length=25,
                                 choices=MESSAGE_STATUS,
                                 default='var',
                                 blank=False,
                                 null=False,
                                 )
    fil_alti = models.CharField(max_length=25,
                                choices=MESSAGE_STATUS,
                                default='var',
                                blank=False,
                                null=False,
                                )
    tecvid = models.CharField(max_length=25,
                              choices=MESSAGE_STATUS,
                              default='var',
                              blank=False,
                              null=False,
                              )
    siyer = models.CharField(max_length=25,
                             choices=MESSAGE_STATUS,
                             default='var',
                             blank=False,
                             null=False,
                             )
    p_arapca = models.CharField(max_length=25,
                                choices=MESSAGE_STATUS,
                                default='var',
                                blank=False,
                                null=False,
                                )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
