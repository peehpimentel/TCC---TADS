# Generated by Django 5.1.2 on 2024-11-21 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoFeed', '0014_alter_noticia_duracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='duracao',
            field=models.PositiveIntegerField(blank=True, default=30, null=True),
        ),
    ]
