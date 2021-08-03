import requests
import json
url = "https://openapi.taifex.com.tw/v1/DailyForeignExchangeRates"



class FiatCurrency(object):
    def __init__(self, base_url=url):
        self.base_url = base_url

    def getUsdtWith(self,targetCurrency):
        search = 'USD/'+str.upper(targetCurrency)
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception('The server has responded with an error')
        response = json.loads(response.text)
        return float(response[-1][search])
