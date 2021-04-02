# Generated by Django 3.1.7 on 2021-04-02 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomapp', '0021_bastanalasuresiarasi'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultdegerler',
            name='BastanAlaSuresiArasi',
            field=models.CharField(choices=[('var', 'Var'), ('yok', 'Yok')], default='var', max_length=25, verbose_name="Baştan A'la Suresine Kadar Olan Sureler"),
        ),
    ]
