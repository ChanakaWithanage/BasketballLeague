# Generated by Django 4.0.3 on 2022-03-17 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_remove_team_team'),
        ('players', '0003_player_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='player', to='teams.team', verbose_name='Team'),
        ),
    ]