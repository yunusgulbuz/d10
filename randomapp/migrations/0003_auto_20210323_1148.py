# Generated by Django 3.1.7 on 2021-03-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomapp', '0002_auto_20210323_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultdegerler',
            name='kk_sayfa_ilk',
            field=models.SmallIntegerField(default=0, verbose_name='Başlangıç'),
        ),
        migrations.AlterField(
            model_name='defaultdegerler',
            name='kk_sayfa_son',
            field=models.SmallIntegerField(default=604, verbose_name='Bitiş'),
        ),
    ]
