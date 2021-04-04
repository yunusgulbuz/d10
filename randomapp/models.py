from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
MESSAGE_STATUS = (
    ('var', 'Var'),
    ('yok', 'Yok'),
)


class Kullanicilar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    KURANIKERIMSayfaIlk = models.SmallIntegerField("KUR'AN-I KERİM Başlangıç Sayfası", default=0, blank=True,null=True)
    KURANIKERIMSayfaSon = models.SmallIntegerField("KUR'AN-I KERİM Bitiş Sayfası", default=600, blank=True,null=True)
    IlmihalIlk = models.SmallIntegerField("İlmihal Başlangıç Sayfası", blank=True, default=0,null=True)
    IlmihalSon = models.SmallIntegerField("İlmihal Bitiş Sayfası", blank=True,default=248,null=True)
    KURANIKERIM = models.CharField("KUR'AN-I KERİM",
                                   max_length=25,
                                   choices=MESSAGE_STATUS,
                                   default='var',
                                   blank=False,
                                   null=False,
                                   )
    Ilmihal = models.CharField("İlmihal",
                               max_length=25,
                               choices=MESSAGE_STATUS,
                               default='var',
                               blank=False,
                               null=False,
                               )
    YasinSuresi = models.CharField("Yasin Suresi",
                                   max_length=25,
                                   choices=MESSAGE_STATUS,
                                   default='var',
                                   blank=False,
                                   null=False,
                                   )
    MulkSuresi = models.CharField("Mülk Suresi",
                                  max_length=25,
                                  choices=MESSAGE_STATUS,
                                  default='var',
                                  blank=False,
                                  null=False,
                                  )
    NebeSuresi = models.CharField("Nebe Suresi",
                                  max_length=25,
                                  choices=MESSAGE_STATUS,
                                  default='var',
                                  blank=False,
                                  null=False,
                                  )
    AlakBeyyineSureleri = models.CharField("Alak-Beyyine Sureleri",
                                           max_length=25,
                                           choices=MESSAGE_STATUS,
                                           default='var',
                                           blank=False,
                                           null=False,
                                           )
    DuhaSuresininAlti = models.CharField("Duha Suresi'nin Altındaki Sureler",
                                         max_length=25,
                                         choices=MESSAGE_STATUS,
                                         default='var',
                                         blank=False,
                                         null=False,
                                         )
    FilSuresininAlti = models.CharField("Fil Suresi'nin Altındaki Sureler",
                                        max_length=25,
                                        choices=MESSAGE_STATUS,
                                        default='var',
                                        blank=False,
                                        null=False,
                                        )
    Tecvid = models.CharField("Tecvid",
                              max_length=25,
                              choices=MESSAGE_STATUS,
                              default='var',
                              blank=False,
                              null=False,
                              )
    SiyeriNebi = models.CharField("Siyer-i Nebi",
                                  max_length=25,
                                  choices=MESSAGE_STATUS,
                                  default='var',
                                  blank=False,
                                  null=False,
                                  )
    PratikArapca = models.CharField("Pratik Arapça",
                                    max_length=25,
                                    choices=MESSAGE_STATUS,
                                    default='var',
                                    blank=False,
                                    null=False,
                                    )
    BastanAlaSuresiArasi = models.CharField("Baştan A'la Suresine Kadar Olan Sureler",
                                            max_length=25,
                                            choices=MESSAGE_STATUS,
                                            default='var',
                                            blank=False,
                                            null=False,
                                            )
    AlaSuresiLeylSuresiArasi = models.CharField("A'la Suresi Leyl Suresi Arası Sureler",
                                                max_length=25,
                                                choices=MESSAGE_STATUS,
                                                default='var',
                                                blank=False,
                                                null=False,
                                                )
    Dualar = models.CharField("Dualar",
                              max_length=25,
                              choices=MESSAGE_STATUS,
                              default='var',
                              blank=False,
                              null=False,
                              )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class KURANIKERIM(models.Model):
    sure_isim = models.CharField(max_length=100, blank=False)
    sayfa = models.SmallIntegerField()
    ayet_no = models.SmallIntegerField()
    ayet = models.TextField(blank=False)

    def __str__(self):
        return f"{self.sure_isim} Suresi {self.ayet_no}. Ayet"


class Ilmihal(models.Model):
    sayfa = models.SmallIntegerField()
    soru = models.TextField(max_length=600, blank=False)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sayfa no : {self.sayfa}"


class SiyeriNebi(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    sayfa = models.SmallIntegerField(blank=True, default=0)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Siyer soru no : {self.pk}"


class Tecvid(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tecvid soru id : {self.pk}"


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


class AlakBeyyineSureleri(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    sure_isim = models.CharField(max_length=150, blank=True)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Alak-Beyyine Sureleri Ayeti id no : {self.pk}"


class FilSuresiNasSuresiArasi(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    sure_isim = models.CharField(max_length=150, blank=True)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Fil Suresi - Nas Suresi Arası id no : {self.pk}"


class DuhaSuresiHumezeSuresiArasi(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    sure_isim = models.CharField(max_length=150, blank=True)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Duha Suresi - Hümeze Suresi Arası id no : {self.pk}"


class BastanAlaSuresiArasi(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    sure_isim = models.CharField(max_length=150, blank=True)
    ayet_no = models.SmallIntegerField(blank=True, null=True)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Baştan A'la Suresi Arası id no : {self.pk}"


class AlaSuresiLeylSuresiArasi(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    sure_isim = models.CharField(max_length=150, blank=True)
    ayet_no = models.SmallIntegerField(blank=True, null=True)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"A'la Suresi Leyl Suresi Arası id no : {self.pk}"


class Dualar(models.Model):
    soru = models.TextField(max_length=600, blank=False)
    aciklama = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dua soru id : {self.pk}"


class KullaniciHesaplari(models.Model):
    email = models.CharField(max_length=100, blank=False)
    sifre = models.CharField(max_length=100, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


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
    ilmihal_id = models.ForeignKey(Ilmihal, blank=False, null=False, on_delete=models.CASCADE)
    kullanici_id = models.ForeignKey(Kullanicilar, blank=False, null=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class s_siyer(models.Model):
    siyer_id = models.ForeignKey(SiyeriNebi, blank=False, null=False, on_delete=models.CASCADE)
    kullanici_id = models.ForeignKey(Kullanicilar, blank=False, null=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class s_tecvid(models.Model):
    tecvid_id = models.ForeignKey(Tecvid, blank=False, null=False, on_delete=models.CASCADE)
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
    KURANIKERIMSayfaIlk = models.SmallIntegerField("KUR'AN-I KERİM Başlangıç Sayfası", default=0, blank=True)
    KURANIKERIMSayfaSon = models.SmallIntegerField("KUR'AN-I KERİM Bitiş Sayfası", default=604, blank=True)
    IlmihalIlk = models.SmallIntegerField("İlmihal Başlangıç Sayfası", blank=True)
    IlmihalSon = models.SmallIntegerField("İlmihal Bitiş Sayfası", blank=True)
    KURANIKERIM = models.CharField("KUR'AN-I KERİM",
                                   max_length=25,
                                   choices=MESSAGE_STATUS,
                                   default='var',
                                   blank=False,
                                   null=False,
                                   )
    Ilmihal = models.CharField("İlmihal",
                               max_length=25,
                               choices=MESSAGE_STATUS,
                               default='var',
                               blank=False,
                               null=False,
                               )
    YasinSuresi = models.CharField("Yasin Suresi",
                                   max_length=25,
                                   choices=MESSAGE_STATUS,
                                   default='var',
                                   blank=False,
                                   null=False,
                                   )
    MulkSuresi = models.CharField("Mülk Suresi",
                                  max_length=25,
                                  choices=MESSAGE_STATUS,
                                  default='var',
                                  blank=False,
                                  null=False,
                                  )
    NebeSuresi = models.CharField("Nebe Suresi",
                                  max_length=25,
                                  choices=MESSAGE_STATUS,
                                  default='var',
                                  blank=False,
                                  null=False,
                                  )
    AlakBeyyineSureleri = models.CharField("Alak-Beyyine Sureleri",
                                           max_length=25,
                                           choices=MESSAGE_STATUS,
                                           default='var',
                                           blank=False,
                                           null=False,
                                           )
    DuhaSuresininAlti = models.CharField("Duha Suresi'nin Altındaki Sureler",
                                         max_length=25,
                                         choices=MESSAGE_STATUS,
                                         default='var',
                                         blank=False,
                                         null=False,
                                         )
    FilSuresininAlti = models.CharField("Fil Suresi'nin Altındaki Sureler",
                                        max_length=25,
                                        choices=MESSAGE_STATUS,
                                        default='var',
                                        blank=False,
                                        null=False,
                                        )
    Tecvid = models.CharField("Tecvid",
                              max_length=25,
                              choices=MESSAGE_STATUS,
                              default='var',
                              blank=False,
                              null=False,
                              )
    SiyeriNebi = models.CharField("Siyer-i Nebi",
                                  max_length=25,
                                  choices=MESSAGE_STATUS,
                                  default='var',
                                  blank=False,
                                  null=False,
                                  )
    PratikArapca = models.CharField("Pratik Arapça",
                                    max_length=25,
                                    choices=MESSAGE_STATUS,
                                    default='var',
                                    blank=False,
                                    null=False,
                                    )
    BastanAlaSuresiArasi = models.CharField("Baştan A'la Suresine Kadar Olan Sureler",
                                            max_length=25,
                                            choices=MESSAGE_STATUS,
                                            default='var',
                                            blank=False,
                                            null=False,
                                            )
    AlaSuresiLeylSuresiArasi = models.CharField("A'la Suresi Leyl Suresi Arası Sureler",
                                                max_length=25,
                                                choices=MESSAGE_STATUS,
                                                default='var',
                                                blank=False,
                                                null=False,
                                                )
    Dualar = models.CharField("Dualar",
                              max_length=25,
                              choices=MESSAGE_STATUS,
                              default='var',
                              blank=False,
                              null=False,
                              )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Varsayılan Ayarlar"
