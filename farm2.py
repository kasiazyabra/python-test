class Animals:
  def __init__(self, type, name, voice, weight):
    self.type = type
    self.name = name
    self.voice = voice
    self.weight = weight
    self.feeded = 'Надо кормить!'
    def feed(self):
      self.feeded = 'Накормили!'

class Milk(Animals):
  def __init__(self, type, name, voice, weight):
    super().__init__(type, name, voice, weight)
    self.milked = 'Надо подоить!'
  def milk(self):
    self.milked = 'Подоили!'

class Wool(Animals):
  def __init__(self, type, name, voice, weight):
    super().__init__(type, name, voice, weight)
    self.cutted = 'Надо постричь!'
  def cut(self):
    self.cutted = 'Постригли!'

class Birds(Animals):
  def __init__(self, type, name, voice, weight):
    super().__init__(type, name, voice, weight)
    self.egged = 'Надо собрать яйца!'
  def eggs(self):
    self.egged = 'Собрали яйца!'

cow1 = Milk('Корова', 'Манька', 'Мууу!', 500)
goat1 = Milk('Коза', 'Рога', 'Меее!', 40)
goat2 = Milk('Коза', 'Копыта', 'Меееее!', 50)
sheep1 = Wool('Овца', 'Барашек', 'Беее!', 60)
sheep2 = Wool('Овца', 'Кудрявый', 'Бебебе!', 70)
chicken1 = Birds('Курица', 'Ко-ко', 'Кококо', 2)
chicken2 = Birds('Курица', 'Кукареку', 'Кукареку', 3)
goose1 = Birds('Гусь', 'Серый', 'Гагага', 4)
goose2 = Birds('Гусь', 'Белый', 'Бугага', 4)
duck1 = Birds('Утка', 'Кряква', 'Кваква', 6)

print(cow1.type)
print(goat2.name)
print(duck1.voice)
print(chicken2.egged)
chicken2.eggs()
print(chicken2.egged)

