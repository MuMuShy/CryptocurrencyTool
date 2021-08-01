import requests
import json

BASE_URL = 'http://api.coincap.io/v2/assets'


class CoinCap(object):
    """
    Object to interact with coincap API
    """

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def _query_coincap(self,endpoint):
        """
        Hits the coincap.io endpoint

        :param endpoint: endpoint to hit
        :return: response as JSON
        """
        response = requests.get(self.base_url+'/'+endpoint)
        if response.status_code != 200:
            raise Exception('The server has responded with an error')
        response = json.loads(response.text)['data']
        return response

    def get_all_coins(self):
        """
        Returns list of all coin tickers
        """
        return self._query_coincap()

    def get_btc_price(self):
        data = self._query_coincap('bitcoin')
        return data['priceUsd']

    def get_eth_price(self):
        data = self._query_coincap('ethereum')
        return data['priceUsd']

    def get_doge_price(self):
        data = self._query_coincap('dogecoin')
        return data['priceUsd']

    def get_custom_price(self,coinid):
        data = self._query_coincap(coinid)
        return data['priceUsd']

    def get_my_combine(self):
        data1 = self._query_coincap('bitcoin')
        data2 = self._query_coincap('ethereum')
        data3 = self._query_coincap('dogecoin')
        return data1['priceUsd']+'/'+data2['priceUsd']+'/'+data3['priceUsd']