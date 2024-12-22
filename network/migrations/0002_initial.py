# Generated by Django 5.1.4 on 2024-12-21 18:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("network", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="networknode",
            name="responsible_user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="network_nodes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Ответственный пользователь",
            ),
        ),
        migrations.AddField(
            model_name="networknode",
            name="supplier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="clients",
                to="network.networknode",
                verbose_name="Поставщик",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="network",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="network.network",
            ),
        ),
    ]