# Generated by Django 4.0.6 on 2022-09-28 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navbar_application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topsection1',
            old_name='sb_title',
            new_name='sub_title',
        ),
        migrations.RenameField(
            model_name='topsection2',
            old_name='sub_title',
            new_name='items',
        ),
    ]
