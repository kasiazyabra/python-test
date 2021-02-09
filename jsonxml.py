def read_json(filename):

  import json
  with open(filename) as f:
    data = json.load(f)

  words = []

  for i in range(len(data['rss']['channel']['items'])):
    words += data['rss']['channel']['items'][i]['description'].split()

  return words

def read_xml(filename):

  import xml.etree.ElementTree as et
  parser = et.XMLParser(encoding='utf-8')
  tree = et.parse(filename, parser)
  root = tree.getroot()
  news_xml = root.findall('channel/item')

  words = []

  for news in news_xml:
    words += news.find('description').text.split()

  return words

def word_count(words, wordlen, wordquant):

  wcount = {}

  for word in words:
    if len(word) > wordlen:
        count = words.count(word)
        wcount.setdefault(count, word)

  wcountkeys = sorted(list(wcount.keys()), reverse=True)

  for i in range(wordquant):
    print(wcount[wcountkeys[i]])

word_count(read_json('newsafr.json'), 6, 10)

word_count(read_xml('newsafr.xml'), 6, 10)

