class AllAnimals:
  totalweight = 0

class MilkAnimals:
  def __init__ (self, type, name, voice, weight):
    self.type = type
    self.name = name
    self.voice = voice
    self.weight = weight
    self.feeded = 'Надо кормить!'
    self.milked = 'Надо подоить!'
    AllAnimals.totalweight += self.weight

class WoolAnimals:
  def __init__ (self, type, name, voice, weight):
    self.type = type
    self.name = name
    self.voice = voice
    self.weight = weight
    self.feeded = 'Надо кормить!'
    self.cutted = 'Надо постричь!'
    AllAnimals.totalweight += self.weight

class Birds:
  def __init__ (self, type, name, voice, weight):
    self.type = type
    self.name = name
    self.voice = voice
    self.weight = weight
    self.feeded = 'Надо кормить!'
    self.egged = 'Надо собрать яйца!'
    AllAnimals.totalweight += self.weight

def feed(self):
    self.feeded = 'Накормили!'

def milk(self):
    self.milked = 'Подоили!'

def cut(self):
    self.cutted = 'Постригли!'

def eggs(self):
    self.egged = 'Собрали яйца!'

cow1 = MilkAnimals('Корова', 'Манька', 'Мууу!', 500)
goat1 = MilkAnimals('Коза', 'Рога', 'Меее!', 40)
goat2 = MilkAnimals('Коза', 'Копыта', 'Меееее!', 50)
sheep1 = WoolAnimals('Овца', 'Барашек', 'Беее!', 60)
sheep2 = WoolAnimals('Овца', 'Кудрявый', 'Бебебе!', 70)
chicken1 = Birds('Курица', 'Ко-ко', 'Кококо', 2)
chicken2 = Birds('Курица', 'Кукареку', 'Кукареку', 3)
goose1 = Birds('Гусь', 'Серый', 'Гагага', 4)
goose2 = Birds('Гусь', 'Белый', 'Бугага', 4)
duck1 = Birds('Утка', 'Кряква', 'Кваква', 6)

print(AllAnimals.totalweight)

