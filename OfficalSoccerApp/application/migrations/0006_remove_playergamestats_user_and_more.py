# Generated by Django 4.1.12 on 2023-11-14 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0005_remove_playergamestats_issued_card_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playergamestats',
            name='user',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='assister',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='assists',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='cardgiven',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='clean_sheets',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='completed_passes',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='goals',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='goalscorer',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='red_card',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='savers',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='saves',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='shutouts',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='total_passes',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='turnovers',
        ),
        migrations.RemoveField(
            model_name='statspergame',
            name='yellow_card',
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dashboardstats',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='statspergame',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
