# Generated by Django 3.1.7 on 2021-03-25 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('randomapp', '0005_auto_20210324_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultdegerler',
            name='kk',
            field=models.CharField(choices=[('var', 'Var'), ('yok', 'Yok')], default='var', max_length=25),
        ),
        migrations.AddField(
            model_name='kullanicilar',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='kullanicilar',
            name='ilmihal_ilk',
            field=models.SmallIntegerField(blank=True, verbose_name='Başlangıç'),
        ),
        migrations.AlterField(
            model_name='kullanicilar',
            name='ilmihal_son',
            field=models.SmallIntegerField(blank=True, verbose_name='Bitiş'),
        ),
        migrations.AlterField(
            model_name='kullanicilar',
            name='kk_sayfa_ilk',
            field=models.SmallIntegerField(blank=True, default=1, verbose_name='Başlangıç'),
        ),
        migrations.AlterField(
            model_name='kullanicilar',
            name='kk_sayfa_son',
            field=models.SmallIntegerField(blank=True, default=600, verbose_name='Bitiş'),
        ),
    ]
