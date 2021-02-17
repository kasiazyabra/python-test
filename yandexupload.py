import requests as requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        resp0 = requests.get('https://cloud-api.yandex.net/v1/disk/resources', params={'path': '/'}, headers={'Authorization': token},)
        resp0.raise_for_status()

        resp1 = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', params={'path': '/1.gif', 'overwrite': 'true'}, headers={'Authorization': token})
        resp1.raise_for_status()

        with open('gifs/1.gif', 'rb') as f:
            resp2 = requests.put(resp1.json()['href'], files={'file': f})
        resp2.raise_for_status()
        
        if resp2.status_code == 201:
            return 'uploaded'
        else:
            return 'something went wrong'

if __name__ == '__main__':
    uploader = YaUploader('<Your Yandex Disk token>')
    result = uploader.upload('c:\my_folder\file.txt')

