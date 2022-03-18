# Generated by Django 4.0.3 on 2022-03-18 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coachesv2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Team Name')),
                ('short_code', models.CharField(max_length=10, null=True, verbose_name='Team Code')),
                ('coach', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='team', to='coachesv2.coach', verbose_name='Coach')),
            ],
        ),
    ]
