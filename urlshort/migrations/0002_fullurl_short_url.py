# Generated by Django 2.1.7 on 2019-03-31 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullurl',
            name='short_url',
            field=models.CharField(default=None, max_length=50),
        ),
    ]