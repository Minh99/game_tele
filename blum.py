
import os
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

class Blum:
    def __init__(self, driver: Chromium):
        self.driver = driver
        self.driver.get('https://web.telegram.org/k/#@BlumCryptoBot')
        # self.driver.run_js('document.body.style.zoom = "70%"')
        self.driver._run_cdp('Input.synthesizePinchGesture', 
            x=0,
            y=0,
            scaleFactor=0.6,
            relativeSpeed=100,  # optional
            gestureSourceType='default'  # optional
        )
        
        self.open_game()
        self.start_iframe()
        
    def start_iframe(self):
        ele = self.driver('.payment-verification', timeout=20)
        # zoom out 50% for iframe
        ele.run_js('document.body.style.zoom = "70%"')
    
        # time.sleep(5)
        
        # get request
        # reqs = self.driver._run_cdp(cmd='Network.enable', cmd_args={'maxPostDataSize': 65536})
        # print(reqs)
        
        div_farming = ele.run_js('return document.querySelector(".time-left")', 10)
        if div_farming:
            print('Farming')
            return
        
        num_try = 1
        while True:
            
            try:
                ele('.reset', timeout=1)
                ele('.reset', timeout=1).click()
            except:
                print('.reset not found {}'.format(num_try))
                pass
            
            try:
                ele('Continue', timeout=1)
                ele('Continue', timeout=1).click()
            except:
                print('Continue not found {}'.format(num_try))
                pass
            
            try:
                div = ele.run_js('return document.querySelector(".kit-fixed-wrapper")', 1)
                div2 = div('tag:div', timeout=1)
                button = div2('tag:button', timeout=1)
                time.sleep(1)
                button.click()
            except:
                print('Claim farming not found {}'.format(num_try))
                pass
            
            try:
                ele('Start farming', timeout=1)
                ele('Start farming', timeout=1).click()
            except:
                print('Start farming not found {}'.format(num_try))
                pass
            
            try:
                ele('.is-fill', timeout=1)
                ele('.is-fill', timeout=1).click()
            except:
                print('is-fill not found {}'.format(num_try))
                pass

            try:
                user_name = ele.run_js('return document.querySelector(".username").innerText', 1)
                
                if (user_name != ''):
                    print('Username: ', user_name)
                    break
            except:
                print('is-fill not found {}'.format(num_try))
                pass
            
            time.sleep(2)
            if num_try == 10:
                break
            
        number = 0
        try:
            ele('.pass', timeout=5)
            time.sleep(2)
            number = ele('.pass', timeout=5).text
            print(number)
        except:
            print('number not found')
            pass
        
        if int(number) > 0:
            print('number > 0')
            
            
        print('Done Blum')

    def open_game(self):
        time.sleep(5)
        try:
            self.driver.run_js('document.getElementsByClassName("is-view")[0].click()', 10)
        except:
            pass
        time.sleep(2)
        try:
            # tab.wait.doc_loaded()
            self.driver.run_js('''document.evaluate("//button[contains(@class, 'popup-button') and contains(., 'Launch')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()''', 10)
        except:
            pass
        finally:
            time.sleep(5)

