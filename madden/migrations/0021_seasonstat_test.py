# Generated by Django 2.2.5 on 2019-10-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madden', '0020_auto_20191001_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='seasonstat',
            name='test',
            field=models.IntegerField(default=0),
        ),
    ]
