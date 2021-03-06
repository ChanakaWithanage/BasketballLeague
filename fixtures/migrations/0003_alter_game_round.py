# Generated by Django 4.0.3 on 2022-03-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0002_alter_playerscore_game_alter_playerscore_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='round',
            field=models.CharField(choices=[('FR', 'First  Round'), ('QF', 'Quarter Final'), ('SF', 'Semi Final'), ('FI', 'Final')], default='QF', max_length=2, verbose_name='game round'),
        ),
    ]
