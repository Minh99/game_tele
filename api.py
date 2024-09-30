

import random
import time
import requests


with open('token.txt', 'r') as file:
    token = file.read()

print('Token sẽ dùng là: ', token)

if not token:
    print('Token not found')
    exit()

res = requests.get('https://game-domain.blum.codes/api/v1/user/balance', headers={
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization':  'Bearer {}'.format(token),
    'lang': 'en',
    'origin': 'https://telegram.blum.codes',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
})

print(res.json())

number_random = random.randint(3, 5)
print('Start play game after {} seconds'.format(number_random))
time.sleep(number_random)

response = requests.post('https://game-domain.blum.codes/api/v1/game/play', headers={
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization':  'Bearer {}'.format(token),
    'lang': 'en',
    'origin': 'https://telegram.blum.codes',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
})

# {
#     "gameId": "af26d338-4228-4882-8b04-5b45521a79eb"
# }

game_id = response.json().get('gameId')

print('Game ID: ', game_id)

number_random = random.randint(7, 13)
print('call now {} seconds'.format(number_random))
time.sleep(number_random)

requests.get('https://game-domain.blum.codes/api/v1/time/now', headers={
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer {}'.format(token),
    'lang': 'en',
    'origin': 'https://telegram.blum.codes',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
})

number_random = random.randint(11, 15)
print('claim after {} seconds'.format(number_random))
time.sleep(number_random)

data = {
    "gameId": "{}".format(game_id),
    "points": random.randint(185, 231)
}

response = requests.post('https://game-domain.blum.codes/api/v1/game/claim', json=data, headers={
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer {}'.format(token),
    'lang': 'en',
    'origin': 'https://telegram.blum.codes',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
})

print('Response Text:', response.text)

time.sleep(10)

res = requests.get('https://game-domain.blum.codes/api/v1/user/balance', headers={
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization':  'Bearer {}'.format(token),
    'lang': 'en',
    'origin': 'https://telegram.blum.codes',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
})

print(res.json())