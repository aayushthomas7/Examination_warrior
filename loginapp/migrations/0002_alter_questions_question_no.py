# Generated by Django 3.2 on 2022-11-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question_no',
            field=models.IntegerField(max_length=20),
        ),
    ]
