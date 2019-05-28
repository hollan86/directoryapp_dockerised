# Generated by Django 2.2.1 on 2019-05-21 23:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('itemType', models.CharField(default='PODCAST', editable=False, max_length=10)),
                ('description', models.TextField(default='')),
                ('duration', models.DurationField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, to='tags.Tag')),
            ],
        ),
    ]
