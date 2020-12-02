class Track:
  def __init__ (self, name, duration: int):
    self.name = name
    self.duration = duration

  def show(self):
    print(f'<{self.name} – {self.duration}>')

class Album:
  def __init__ (self, name, artist):
    self.name = name
    self.artist = artist
    self.tracklist = []
    self.duration = 0

  def add_track(self, track):
    self.tracklist.append(track)
    self.duration += track.duration

  def get_tracks(self):
    for track in self.tracklist:
      track.show()

  def get_duration(self):
    print(self.duration)


track1 = Track('Тяжелый митал', 6)
track2 = Track('Очень тяжелый митал', 13)
track3 = Track('Пение всеумиленное для котиков', 777)
album1 = Album('Первый альбом', 'Адская сотона')
album2 = Album('Второй альбом', 'Православные песнопения')

track1.show()
track2.show()
track3.show()
album1.add_track(track1)
album1.add_track(track2)
album2.add_track(track3)
album1.get_tracks()
album2.get_tracks()
album1.get_duration()
album2.get_duration()

