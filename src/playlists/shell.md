```python
from src.playlists.models import Playlist
from src.videos.models import Video

video_1 = Video.objects.create(title='Video_title', video_id='123abc')

print(video_1)

print(dir(video_1))

playlist_1 = Playlist.objects.create(title='This is my title', video=video_1)

print(dir(playlist_1))

print(playlist_1.video_id)

print(video_1.id)
```

```python
playlist_1.video = None
playlist_1.save()
print(playlist_1.video_id)
print(video_1.playlist_set.all())
```

```python
playlist_1.video = video_1
playlist_1.save()
print(video_1.playlist_set.all())
print(playlist_1.id)
```


```python
print(video_1.playlist_set.all().published())

print(Playlist.objects.all().published())

print(Playlist.objects.filter(video=video_1).published())
```