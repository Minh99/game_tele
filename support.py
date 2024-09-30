
import os
import random
import time

from DrissionPage import Chromium, ChromiumOptions
from get_proxy import Proxy


chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # 请改为你电脑内Chrome可执行文件路径
driver_path = r'D:\Downloads\acc_teles\1_Tool_NV\chromedriver-win64\chromedriver.exe'  # 请改为你电脑内chromedriver.exe路径
extension = r'D:\Downloads\acc_teles\1_Tool_NV\extension'


folders = [27793894707,27794165748,27794167573,27794234348,27794244331,27794853692,27795490857,27795524007]
# loop mkdir
# for folder in folders:
#     os.mkdir(f'./profiles/{folder}')

proxies = ['43.228.237.55:6001', '91.123.11.130:6396', '92.112.238.217:7096', '104.239.3.107:6067', '85.198.36.21:5658', '104.239.19.140:6817', '45.249.106.214:5911', '45.43.191.192:6153', '92.112.236.32:6464', '172.98.178.9:6082', '216.74.80.247:6819', '84.247.60.162:6132', '45.41.173.225:6592', '107.181.128.230:5242', '103.99.34.106:6721']
proxies_with_folder = []
start_port = 9655

for folder in folders:
    random_proxy = random.choice(proxies)
    print('====================')
    print('proxy {}'.format(random_proxy))
    print('folder {}'.format(folder))
    print('start_port {}'.format(start_port))
    print('====================')
    
    co = ChromiumOptions()
    co.set_browser_path(chrome_path)
    co.set_local_port(start_port)
    start_port += 1
    co.set_user_data_path(r'D:\Downloads\acc_teles\1_Tool_NV\profiles\{}'.format(folder))
    co.set_proxy(random_proxy)
    co.set_argument('--window-size', '800, 600')
    # maximum screen size
    # co.set_argument('--start-maximized')
    co.set_pref('credentials_enable_service', False)
    co.mute()
    # co.set_load_mode('eager')
    
    browser = Chromium(co)
    # browser.set.retry_times(5)
    
    tab = browser.latest_tab
    
    tab.get('https://web.telegram.org/k/')
    tab.run_js('document.body.style.zoom = "70%"')
    
    while True:
        is_logged_in = tab.run_js('return Boolean(document.querySelector("#telegram-search-input"))')
        is_logged = tab.run_js('return Boolean(document.querySelector(".input-search"))')
        time.sleep(1)
        if is_logged_in or is_logged:
            break
    
    tab.close()
    browser.quit()
    
    
    
    
