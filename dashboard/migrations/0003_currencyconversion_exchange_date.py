# Generated by Django 5.2.3 on 2025-07-18 08:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_rename_rate_currency_parts_currency_parts_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="currencyconversion",
            name="exchange_date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
