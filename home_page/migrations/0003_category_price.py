# Generated by Django 4.0.6 on 2022-09-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_remove_category_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Price'),
        ),
    ]
