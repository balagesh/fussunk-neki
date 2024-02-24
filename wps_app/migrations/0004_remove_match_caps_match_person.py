# Generated by Django 5.0.2 on 2024-02-21 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wps_app', '0003_remove_person_match_match_caps_alter_movie_cast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='caps',
        ),
        migrations.AddField(
            model_name='match',
            name='person',
            field=models.ManyToManyField(related_name='matches', to='wps_app.person'),
        ),
    ]