# Generated by Django 2.2.5 on 2019-09-09 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madden', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GameStats',
            new_name='GameStat',
        ),
        migrations.RenameModel(
            old_name='PlayerStats',
            new_name='PlayerStat',
        ),
        migrations.RenameModel(
            old_name='SeasonStats',
            new_name='SeasonStat',
        ),
    ]
