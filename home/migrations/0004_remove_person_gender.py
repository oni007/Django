# Generated by Django 4.0.1 on 2022-01-23 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_person_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='gender',
        ),
    ]