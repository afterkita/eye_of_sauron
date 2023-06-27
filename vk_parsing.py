import requests
import config

version = 5.131
domain = 'esportsbfu'

response = requests.get('https://api.vk.com/method/users.get',
                        params={
                            'access_token': config.VK_TOKEN,
                            'v': version,
                            'user_ids': 'rekryt98',
                            'fields': 'education,sex'       #Писать через запитую
                        }
                        )
data = response.json()
print(1)

