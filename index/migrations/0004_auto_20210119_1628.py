# Generated by Django 3.1.5 on 2021-01-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_appdetail_app_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdetail',
            name='app_desc',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
