import requests

token = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'

class VkUser:

    url = 'https://api.vk.com/method/'

    def __init__(self, user_id, token, version):
        self.user_id = user_id
        self.token = token
        self.version = version
        self.params = {
            'access_token' : self.token,
            'v' : self.version
        }
        self.owner_id = requests.get(self.url + 'users.get', self.params).json()['response'][0]['id']

    def __repr__(self):
      id = "http://vk.com/id" + str(self.user_id)
      return id
    
    def __and__(self, other):
      intersection = set(self.friends_get()['response']['items']) & set(other.friends_get()['response']['items'])
      for i in intersection:
        print(VkUser(i, token, 5.21))

    def friends_get (self, user_id=None):
        if user_id is None:
            user_id = self.user_id
        friends_url = self.url + 'friends.get'
        friends_params = {
            'count' : 1000,
            'user_id' : user_id
        }
        resp = requests.get(friends_url, params={**self.params, **friends_params})
        return resp.json()

user1 = VkUser(147633933, token, 5.21)
user2 = VkUser(56, token, 5.21)

print(user1)
print(user2)
print(user1 & user2)

