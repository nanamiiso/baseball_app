# Generated by Django 5.0.1 on 2024-02-26 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseball_app', '0010_event_away_team_event_home_team_event_stadium_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
    ]
