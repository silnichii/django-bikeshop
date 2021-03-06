# Generated by Django 2.1.3 on 2018-11-24 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bikes',
            options={'verbose_name_plural': 'Bikes'},
        ),
        migrations.AlterModelOptions(
            name='types',
            options={'verbose_name_plural': 'Types'},
        ),
        migrations.RemoveField(
            model_name='bikes',
            name='type',
        ),
        migrations.AddField(
            model_name='bikes',
            name='type_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bikes.Types'),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='brand',
            field=models.CharField(default='Unknown brand', max_length=100),
        ),
    ]
