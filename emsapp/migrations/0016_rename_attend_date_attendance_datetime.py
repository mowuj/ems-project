# Generated by Django 4.1.4 on 2022-12-15 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emsapp', '0015_rename_datetime_attendance_attend_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='attend_date',
            new_name='datetime',
        ),
    ]