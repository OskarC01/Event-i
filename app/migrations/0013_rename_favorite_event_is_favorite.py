# Generated by Django 4.1.1 on 2022-12-20 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_event_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='favorite',
            new_name='is_favorite',
        ),
    ]