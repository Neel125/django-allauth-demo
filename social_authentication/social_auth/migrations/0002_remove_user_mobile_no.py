# Generated by Django 3.2.4 on 2021-06-20 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile_no',
        ),
    ]
