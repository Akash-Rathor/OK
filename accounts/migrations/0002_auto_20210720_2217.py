# Generated by Django 3.2.5 on 2021-07-20 16:47

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturls',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='shorturls',
            name='delete_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=datetime.datetime(2021, 8, 19, 22, 16, 51, 955201)),
            preserve_default=False,
        ),
    ]
