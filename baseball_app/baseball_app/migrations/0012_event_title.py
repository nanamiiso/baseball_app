# Generated by Django 5.0.1 on 2024-02-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball_app', '0011_remove_event_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
