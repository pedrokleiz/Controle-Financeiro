# Generated by Django 3.1.2 on 2020-10-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_name', models.CharField(max_length=50)),
                ('deposit_value', models.DecimalField(
                    decimal_places=2, max_digits=19)),
                ('deposit_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('withdrawal_name', models.CharField(max_length=50)),
                ('withdrawal_value', models.DecimalField(
                    decimal_places=2, max_digits=19)),
                ('withdrawal_date', models.DateTimeField(
                    auto_now=True)),
            ],
        ),
    ]