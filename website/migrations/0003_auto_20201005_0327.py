# Generated by Django 3.1.2 on 2020-10-05 06:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20201005_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='deposit_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='withdrawal_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
