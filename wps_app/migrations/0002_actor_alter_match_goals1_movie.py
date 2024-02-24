# Generated by Django 5.0.2 on 2024-02-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wps_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='match',
            name='goals1',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cast', models.ManyToManyField(related_name='movies', to='wps_app.actor')),
            ],
        ),
    ]
