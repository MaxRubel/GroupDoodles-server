# Generated by Django 5.1 on 2024-08-14 00:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupdoodles_api', '0002_doodle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('colors', models.JSONField()),
                ('date_created', models.DateField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groupdoodles_api.user')),
            ],
        ),
    ]
