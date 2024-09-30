import os
import random
import threading
import time
from DrissionPage import *
from DrissionPage.errors import *
from DrissionPage.common import *
from DrissionPage.items import *
from DrissionPage import Chromium
from DrissionPage import ChromiumOptions
from DrissionPage.common import Settings
from DrissionPage.common import Keys
from DrissionPage.common import By
from DrissionPage.errors import ElementNotFoundError
from requests import request
from blum import Blum
from tomato import Tomato

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # 请改为你电脑内Chrome可执行文件路径
driver_path = r'D:\Downloads\acc_teles\1_Tool_NV\chromedriver-win64\chromedriver.exe'  # 请改为你电脑内chromedriver.exe路径
extension = r'D:\Downloads\acc_teles\1_Tool_NV\extension'

user_agents = [
    'Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1',
    'Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1',
    'Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1'
]

class Game:
    def __init__(self, profile, proxy, game, port):
        
        self.profile = profile
        self.proxy = proxy
        self.game = game
        
        co = ChromiumOptions()
        co.set_browser_path(chrome_path)
        co.set_local_port(port)
        co.set_user_data_path(profile)
        co.set_proxy(proxy)
        co.add_extension(extension)
        co.set_argument('--window-size', '200,600')
        # co.set_user_agent(random.choice(user_agents))
        # co.set_argument('--load-extension={}'.format(extension))
        # random position at in screen symtem
        # co.set_argument('--window-position', '{},{}'.format(random.randint(0, 1000), 0))
        co.set_pref('credentials_enable_service', False)
        # co.set_load_mode('eager')
        
        self.browser = Chromium(co)
        self.browser.set.retry_times(5)
        
        self.tab = self.browser.latest_tab
            
        # self.tab.set.load_mode.eager()
        print(self.tab.title)
        if self.game == 'blum':
            self.start_blum()
            self.stop_driver()
        if self.game == 'tomato':
            self.start_tomato()
            # self.stop_driver()
    
    def start_blum(self):
        print('startBlum with profile: {} - proxy: {}'.format(self.profile, self.proxy))
        Blum(self.tab)
        
    def start_tomato(self):
        print('startTomato with profile: {} - proxy: {}'.format(self.profile, self.proxy))
        Tomato(self.tab)
    
    def stop_driver(self):
        time.sleep(2)
        self.browser.quit()  
        print('Driver stopped {} - {}'.format(self.profile, self.proxy))
        
    # tab.close()

import concurrent.futures
from get_proxy import Proxy

if __name__ == '__main__':
    api_key2 = ''
    
    # proxies1 = []
    # proxies2 = Proxy(api_key2).get_proxies()
   
    proxies = []

    start_port = 9223
    
    # get folder name in profiles
    folders = []
    for folder in os.listdir(r'D:\Downloads\acc_teles\1_Tool_NV\profiles'):
        folders.append(folder)
    
    # folders = folders[:2]
    print(folders)
    
    if len(folders) == 0:
        print('No folder found')
        exit()
    
    threads = []
    max_workers = 10
    #  wait checkin .username .balance
        
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        # loop folders with index element
        for index, folder in enumerate(folders):
            random_proxy = random.choice(proxies)
            profile = r'D:\Downloads\acc_teles\1_Tool_NV\profiles\{}'.format(folder)
            future = executor.submit(Game, profile, random_proxy, 'blum', start_port)
            futures.append(future)
            start_port += 1

        # Chờ tất cả hoàn thành
        for future in concurrent.futures.as_completed(futures):
           future.result()

    # if int(number) > 0:
    #     print('number > 0')
        # ele('.play-btn').click()
        
        
        # accept:application/json, text/plain, */*
        # accept-language:en-US,en;q=0.9
        # authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJoYXNfZ3Vlc3QiOmZhbHNlLCJ0eXBlIjoiQUNDRVNTIiwiaXNzIjoiYmx1bSIsInN1YiI6IjQ3ZjNhODBlLTVhNTAtNDhmNC05ZDMzLThmZGMwNzVkYzQxOCIsImV4cCI6MTcyNzM3MTUwOCwiaWF0IjoxNzI3MzY3OTA4fQ.8leXflOExXUcJ9bOu5CqbBcIwWwJiHvdyg2cqavjeMM
        # content-length:0
        # lang:en
        # origin:https://telegram.blum.codes
        # priority:u=1, i
        # sec-ch-ua:"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"
        # sec-ch-ua-mobile:?0
        # sec-ch-ua-platform:"Windows"
        # sec-fetch-dest:empty
        # sec-fetch-mode:cors
        # sec-fetch-site:same-site
        # user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36
        
        # read file .txt
        
        # print('Bạn có 30s để lấy token từ trình duyệt, tìm kiếm API /me để lấy giá trị authorization (bỏ BEARER)')
        
        # time.sleep(30)
        # with open('token.txt', 'r') as file:
        #     token = file.read()
            
        # print('Token sẽ dùng là: ', token)
        
        # number_run = int(number)
        
        # for i in range(number_run):
        
        #     request('GET', 'https://game-domain.blum.codes/api/v1/user/balance', headers={
        #         'accept': 'application/json, text/plain, */*',
        #         'accept-language': 'en-US,en;q=0.9',
        #         'authorization':  'Bearer {}'.format(token),
        #         'lang': 'en',
        #         'origin': 'https://telegram.blum.codes',
        #         'priority': 'u=1, i',
        #         'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'same-site',
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        #     })
            
        #     number_random = random.randint(3, 5)
        #     time.sleep(number_random)
            
        #     response = request('POST', 'https://game-domain.blum.codes/api/v1/game/play', headers={
        #         'accept': 'application/json, text/plain, */*',
        #         'accept-language': 'en-US,en;q=0.9',
        #         'authorization':  'Bearer {}'.format(token),
        #         'lang': 'en',
        #         'origin': 'https://telegram.blum.codes',
        #         'priority': 'u=1, i',
        #         'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'same-site',
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        #     })
            
        #     # {
        #     #     "gameId": "af26d338-4228-4882-8b04-5b45521a79eb"
        #     # }
            
        #     game_id = response.json().get('gameId')
            
        #     print('Game ID: ', game_id)
            
        #     number_random = random.randint(7, 13)
        #     time.sleep(number_random)
            
        #     request('GET', 'https://game-domain.blum.codes/api/v1/time/now', headers={
        #         'accept': 'application/json, text/plain, */*',
        #         'accept-language': 'en-US,en;q=0.9',
        #         'authorization': 'Bearer {}'.format(token),
        #         'lang': 'en',
        #         'origin': 'https://telegram.blum.codes',
        #         'priority': 'u=1, i',
        #         'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'same-site',
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        #     })
            
        #     number_random = random.randint(11, 15)
        #     time.sleep(number_random)
            
        #     data = {
        #         "gameId": game_id,
        #         "points": random.randint(185, 231)
        #     }
            
        #     request('POST', 'https://game-domain.blum.codes/api/v1/game/claim', headers={
        #         'accept': 'application/json, text/plain, */*',
        #         'accept-language': 'en-US,en;q=0.9',
        #         'authorization': 'Bearer {}'.format(token),
        #         'lang': 'en',
        #         'origin': 'https://telegram.blum.codes',
        #         'priority': 'u=1, i',
        #         'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'same-site',
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        #     }, data=data)
            
        