# Generated by Django 4.0.6 on 2022-09-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerheading',
            name='heading_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
