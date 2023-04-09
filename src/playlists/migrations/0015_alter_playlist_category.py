# Generated by Django 3.2.18 on 2023-04-01 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('playlists', '0014_playlist_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='playlists', to='categories.category'),
        ),
    ]
