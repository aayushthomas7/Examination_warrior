# Generated by Django 3.2 on 2022-12-06 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0007_auto_20221127_0229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={'ordering': ('quiz', 'question_no')},
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
    ]
