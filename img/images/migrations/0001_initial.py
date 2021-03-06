# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-03-15 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.CharField(max_length=50)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('target_id', models.AutoField(primary_key=True, serialize=False)),
                ('alphanumeric', models.CharField(max_length=1)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Image')),
            ],
        ),
    ]
