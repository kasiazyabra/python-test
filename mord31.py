fileslist = ['1.txt', '2.txt', '3.txt']
fileslen = {}

for files in fileslist:
  with open(files) as f:
    lines = f.readlines()
    fileslen.setdefault(len(lines), files)

keylist = list(fileslen.keys())
keylist.sort()
for i in keylist:
  with open('file.txt', 'a') as document:
    document.write(f'{fileslen[i]}\n{i}\n')
    with open(fileslen[i]) as f:
      document.write(f.read())

