# Generated by Django 3.2.15 on 2025-06-14 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='адрес')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='широта')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='долгота')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='обновлено')),
            ],
            options={
                'verbose_name': 'место на карте',
                'verbose_name_plural': 'места на карте',
            },
        ),
    ]
