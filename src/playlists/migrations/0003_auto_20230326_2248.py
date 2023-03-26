# Generated by Django 3.2.18 on 2023-03-26 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_alter_video_video_id'),
        ('playlists', '0002_playlist_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='videos',
            field=models.ManyToManyField(blank=True, related_name='playlist_item', to='videos.Video'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='videos.video'),
        ),
    ]
