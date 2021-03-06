# Generated by Django 3.1.7 on 2021-03-31 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomapp', '0012_auto_20210328_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='beyyine',
            new_name='AlakSuresi',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='duha_alti',
            new_name='BeyyineSuresi',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='fil_alti',
            new_name='DuhaSuresininAlti',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='igra',
            new_name='FilSuresininAlti',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='ilmihal_ilk',
            new_name='IlmihalIlk',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='ilmihal_son',
            new_name='IlmihalSon',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='kk',
            new_name='KURANIKERIM',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='kk_sayfa_ilk',
            new_name='KURANIKERIMSayfaIlk',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='kk_sayfa_son',
            new_name='KURANIKERIMSayfaSon',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='mulk',
            new_name='MulkSuresi',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='nebe',
            new_name='NebeSuresi',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='p_arapca',
            new_name='PratikArapca',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='siyer',
            new_name='SiyeriNebi',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='tecvid',
            new_name='Tecvid',
        ),
        migrations.RenameField(
            model_name='defaultdegerler',
            old_name='yasin',
            new_name='YasinSuresi',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='beyyine',
            new_name='AlakSuresi',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='duha_alti',
            new_name='BeyyineSuresi',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='fil_alti',
            new_name='DuhaSuresininAlti',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='igra',
            new_name='FilSuresininAlti',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='ilmihal_ilk',
            new_name='IlmihalIlk',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='ilmihal_son',
            new_name='IlmihalSon',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='kk_sayfa_ilk',
            new_name='KURANIKERIMSayfaIlk',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='kk_sayfa_son',
            new_name='KURANIKERIMSayfaSon',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='mulk',
            new_name='MulkSuresi',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='nebe',
            new_name='NebeSuresi',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='p_arapca',
            new_name='PratikArapca',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='siyer',
            new_name='SiyeriNebi',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='tecvid',
            new_name='Tecvid',
        ),
        migrations.RemoveField(
            model_name='kullanicilar',
            name='yasin',
        ),
        migrations.AddField(
            model_name='kullanicilar',
            name='YasinSuresi',
            field=models.CharField(blank=True, choices=[('var', 'Var'), ('yok', 'Yok')], default='var', max_length=25, null=True, verbose_name='Yasin Suresi'),
        ),
    ]
