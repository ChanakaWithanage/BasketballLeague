# Generated by Django 4.0.3 on 2022-03-20 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Coach'), (3, 'Player')], default=1),
        ),
    ]
