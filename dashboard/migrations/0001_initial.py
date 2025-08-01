# Generated by Django 5.2.3 on 2025-07-15 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("symbol", models.CharField(max_length=10)),
                ("rate", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="CurrencyConversion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.FloatField(default=0.0)),
                (
                    "currency1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="currency1",
                        to="dashboard.currency",
                    ),
                ),
                (
                    "currency2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="currency2",
                        to="dashboard.currency",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UnitConversion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.FloatField(default=0.0)),
                (
                    "unit1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="unit1",
                        to="dashboard.unit",
                    ),
                ),
                (
                    "unit2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="unit2",
                        to="dashboard.unit",
                    ),
                ),
            ],
        ),
    ]
