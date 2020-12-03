class Track:
  def __init__ (self, name, duration: int):
    self.name = name
    self.duration = duration

  def __str__(self):
    return (f'{self.name}–{self.duration}')

  def __gt__(self,other):
    return self.duration > other.duration
  
class Album:
  def __init__ (self, name, artist):
    self.name = name
    self.artist = artist
    self.tracklist = []
    self.duration = 0

  def __str__(self):
    tracklist = ''
    for tracks in self.tracklist:
      tracklist += (f'\t {str(tracks)} \n')
    return f'Name group: {self.name} \nName album: {self.artist}\nTracks:\n{tracklist}'

  def add_track(self, track):
    self.tracklist.append(track)
    self.duration += track.duration

  def get_tracks(self):
    for track in self.tracklist:
      print(track)

  def get_duration(self):
    print(self.duration)

track1 = Track('Тяжелый митал', 6)
track2 = Track('Очень тяжелый митал', 13)
track3 = Track('Пение всеумиленное для котиков', 777)
album1 = Album('Первый альбом', 'Адская сотона')
album2 = Album('Второй альбом', 'Православные песнопения')

album1.add_track(track1)
album1.add_track(track2)
album2.add_track(track3)

print(album1)
print(album2)

print(track1 > track2)

