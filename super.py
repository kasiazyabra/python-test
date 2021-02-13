import requests

url = 'https://superheroapi.com/api/'
token = '2619421814940190'
heroes = ['Hulk', 'Captain America', 'Thanos']
maxintelligence = 0
mostintelligenthero = ''

for name in heroes:
  response = requests.get(url + token + '/search/' + name)
  name = response.json()['results'][0]['name']
  intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
  if intelligence > maxintelligence:
    maxintelligence = intelligence
    mostintelligenthero = name

print(mostintelligenthero)


