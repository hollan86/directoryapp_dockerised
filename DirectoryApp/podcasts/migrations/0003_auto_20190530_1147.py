# Generated by Django 2.2.1 on 2019-05-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0002_podcast_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='duration',
            field=models.DurationField(blank=True),
        ),
    ]
