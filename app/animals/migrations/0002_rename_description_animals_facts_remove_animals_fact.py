# Generated by Django 4.1.13 on 2023-11-03 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animals',
            old_name='description',
            new_name='facts',
        ),
        migrations.RemoveField(
            model_name='animals',
            name='fact',
        ),
    ]
