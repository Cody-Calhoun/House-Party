# Generated by Django 3.1.3 on 2020-12-15 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
