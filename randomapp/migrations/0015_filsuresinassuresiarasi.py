# Generated by Django 3.1.7 on 2021-04-01 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomapp', '0014_auto_20210401_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilSuresiNasSuresiArasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soru', models.TextField(max_length=600)),
                ('sure_isim', models.CharField(blank=True, max_length=150)),
                ('aciklama', models.CharField(blank=True, max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
