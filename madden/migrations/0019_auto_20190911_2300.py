# Generated by Django 2.2.5 on 2019-09-11 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madden', '0018_auto_20190910_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='season',
            field=models.PositiveIntegerField(default=2019),
        ),
    ]
