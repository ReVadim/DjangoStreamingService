# Generated by Django 3.2.18 on 2023-03-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_videoproxy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VideoProxy',
        ),
        migrations.CreateModel(
            name='VideoAllProxy',
            fields=[
            ],
            options={
                'verbose_name': 'All Video',
                'verbose_name_plural': 'All Videos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('videos.video',),
        ),
        migrations.CreateModel(
            name='VideoPublishedProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Published Video',
                'verbose_name_plural': 'Published Videos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('videos.video',),
        ),
        migrations.AddField(
            model_name='video',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
