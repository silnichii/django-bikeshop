# Generated by Django 2.1.3 on 2018-12-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0002_auto_20181124_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
