# Generated by Django 3.1.7 on 2021-03-26 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomapp', '0007_auto_20210326_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='yasin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soru', models.TextField(max_length=600)),
                ('aciklama', models.CharField(blank=True, max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
