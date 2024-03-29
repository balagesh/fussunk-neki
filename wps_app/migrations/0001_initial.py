# Generated by Django 5.0.2 on 2024-02-20 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=50)),
                ('team2', models.CharField(max_length=50)),
                ('goals1', models.IntegerField(default=0)),
                ('goals2', models.IntegerField(default=0)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('match', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wps_app.match')),
            ],
        ),
    ]
