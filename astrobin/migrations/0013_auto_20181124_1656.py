# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-11-24 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin', '0012_auto_20181117_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='commercialgear',
            name='description_en_GB',
            field=models.TextField(blank=True, help_text='Here you can write the full commercial description of your product. You can use some <a href="/faq/#comments">formatting rules</a>.', null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='commercialgear',
            name='tagline_en_GB',
            field=models.CharField(blank=True, help_text='A memorable phrase that will sum up this product, for marketing purposes.', max_length=256, null=True, verbose_name='Tagline'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.CharField(blank=True, choices=[(b'en', 'English (US)'), (b'en-GB', 'English (GB)'), (b'it', 'Italian'), (b'es', 'Spanish'), (b'fr', 'French'), (b'fi', 'Finnish'), (b'de', 'German'), (b'nl', 'Dutch'), (b'tr', 'Turkish'), (b'sq', 'Albanian'), (b'pl', 'Polish'), (b'pt-BR', 'Brazilian Portuguese'), (b'el', 'Greek'), (b'ru', 'Russian'), (b'ar', 'Arabic'), (b'ja', 'Japanese')], max_length=8, null=True, verbose_name='Language'),
        ),
    ]
