import requests

class Proxy:
    def __init__(self, api_key):
        self.api_key = api_key
        self.proxies = []
        self.url = "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25"

    def get_proxies(self):
        response = requests.get(
            self.url,
            headers={ "Authorization": "Token {}". format(self.api_key) }
        )
        
        list_proxies = response.json().get('results')
        for proxy in list_proxies:
            if proxy.get('valid') == True:
                self.proxies.append('{}:{}'.format(proxy.get('proxy_address'), proxy.get('port')))

        return self.proxies
