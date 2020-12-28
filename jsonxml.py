def read_json():

  import json
  with open('newsafr.json') as f:
    data = json.load(f)

  words = []

  for i in range(len(data['rss']['channel']['items'])):
    words += data['rss']['channel']['items'][i]['description'].split()

  return words

def read_xml():

  import xml.etree.ElementTree as et
  parser = et.XMLParser(encoding='utf-8')
  tree = et.parse('newsafr.xml', parser)
  root = tree.getroot()
  news_xml = root.findall('channel/item')

  words = []

  for news in news_xml:
    words += news.find('description').text.split()

  return words

def word_count(words):

  wlonguniq = []
  wcount = {}

  for word in words:
    if word not in wlonguniq and len(word) > 6:
      wlonguniq.append(word)

  for word1 in wlonguniq:
    count = 0
    for word2 in words:
      if word1 == word2:
        count += 1
    if count > 1:
      wcount.setdefault(count, word1)

  wcountkeys = sorted(list(wcount.keys()), reverse=True)

  for i in range(10):
    print(wcount[wcountkeys[i]])

word_count(read_json())

word_count(read_xml())

