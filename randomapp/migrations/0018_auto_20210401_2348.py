# Generated by Django 3.1.7 on 2021-04-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomapp', '0017_auto_20210401_2342'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AlakBeyyineSuresi',
            new_name='AlakBeyyineSureleri',
        ),
        migrations.RemoveField(
            model_name='defaultdegerler',
            name='AlakSuresi',
        ),
        migrations.RemoveField(
            model_name='defaultdegerler',
            name='BeyyineSuresi',
        ),
        migrations.RemoveField(
            model_name='kullanicilar',
            name='AlakSuresi',
        ),
        migrations.RemoveField(
            model_name='kullanicilar',
            name='BeyyineSuresi',
        ),
        migrations.AddField(
            model_name='defaultdegerler',
            name='AlakBeyyineSureleri',
            field=models.CharField(choices=[('var', 'Var'), ('yok', 'Yok')], default='var', max_length=25, verbose_name='Alak-Beyyine Sureleri'),
        ),
        migrations.AddField(
            model_name='kullanicilar',
            name='AlakBeyyineSureleri',
            field=models.CharField(blank=True, choices=[('var', 'Var'), ('yok', 'Yok')], default='var', max_length=25, null=True, verbose_name='Alak-Beyyine Sureleri'),
        ),
    ]