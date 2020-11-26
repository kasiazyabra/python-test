class Track:
  def __init__ (self, name, duration):
    self.name = name
    self.duration = duration

def show(Track):
  print(f'<{Track.name}–{Track.duration}>')

class Album:
  def __init__ (self, name, artist):
    self.name = name
    self.artist = artist
    self.tracklist = []
    self.duration = 0

def add_track(Album, Track):
  Album.tracklist.append(Track.name)
  Album.duration += Track.duration

def get_duration(Album):
  print(Album.duration)

def get_tracks(Album):
  print(Album.tracklist)

track1 = Track('Тяжелый митал', 6)
track2 = Track('Очень тяжелый митал', 13)
track3 = Track('Пение всеумиленное для котиков', 777)
album1 = Album('Первый альбом', 'Адская сотона')
album2 = Album('Второй альбом', 'Православные песнопения')

show(track1)
show(track2)
show(track3)
add_track(album1,track1)
add_track(album1,track2)
add_track(album2,track3)
get_tracks(album1)
get_tracks(album2)
get_duration(album1)
get_duration(album2)

