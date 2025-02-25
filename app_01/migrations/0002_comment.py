# Generated by Django 4.2.5 on 2024-04-22 06:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('updated', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('published', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_01.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_01.author')),
            ],
        ),
    ]
