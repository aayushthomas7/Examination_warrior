# Generated by Django 3.2 on 2022-12-06 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0009_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score_val',
            field=models.IntegerField(null=True),
        ),
    ]