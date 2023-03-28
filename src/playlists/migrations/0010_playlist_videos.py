# Generated by Django 3.2.18 on 2023-03-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_alter_video_video_id'),
        ('playlists', '0009_remove_playlist_videos'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='videos',
            field=models.ManyToManyField(blank=True, related_name='playlist_item', through='playlists.PlaylistItem', to='videos.Video'),
        ),
    ]