import operator

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
      if word not in wcount:
        wcount.setdefault(word, 1)
      else:
        cnt = wcount[word] + 1
        upd = {word:cnt}
        wcount.update(upd)
  
  wsorted = sorted(wcount.items(), key=operator.itemgetter(1), reverse=True)

  for i in range(wordquant):
    print(wsorted[i])

word_count(read_json('newsafr.json'), 6, 10)
word_count(read_xml('newsafr.xml'), 6, 10)

