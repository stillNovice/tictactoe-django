# Generated by Django 2.0.6 on 2018-06-28 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('first_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_first_player', to=settings.AUTH_USER_MODEL)),
                ('second_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_second_player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('comments', models.CharField(blank=True, max_length=300)),
                ('move_by_first_player', models.BooleanField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplay.Game')),
            ],
        ),
    ]