# Generated by Django 5.1.7 on 2025-03-24 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='followers',
            new_name='following',
        ),
    ]
