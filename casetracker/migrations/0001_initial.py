# Generated by Django 3.1.5 on 2021-03-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borough_name', models.CharField(max_length=30)),
                ('vaccines_given', models.CharField(max_length=30)),
            ],
        ),
    ]