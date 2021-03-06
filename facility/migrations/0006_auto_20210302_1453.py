# Generated by Django 3.1.5 on 2021-03-02 14:53
from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'export.json'
def load_data(apps, schema_editor):
    Clinic = apps.get_model('facility', 'Clinic')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name','no-name')
                    longitude = obj.get('lat', 0)
                    latitude = obj.get('lon', 0)
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                    Clinic(name=name, location = location).save()
            except KeyError:
                pass     

class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0005_auto_20210302_1427'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]


