import requests
import json
from YahooPy.StockClass import Stock
class Client:

    def __init__(self, proxy=None) -> None:
        self.base_url = "https://query2.finance.yahoo.com/"
        self.proxy = proxy
        pass

    def check_valid_interval(self, interval:str="1m"):
        if interval not in ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]:
            raise ValueError('You eneterd invalid interval - please insert one of the following \n["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]')
        return True

    def format_proxy(self):
        if self.proxy:
            proxies = {
                "http":f"http://{self.proxy}/",
                "https":f"https://{self.proxy}/",
            }
            return proxies
        return None
    
    def get_stock(self, symbols:list, interval:str="1m", range:str="1m"):
        self.check_valid_interval(interval=interval)

        headers={
            "host": "query2.finance.yahoo.com",
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }
        params = {
            "symbols":",".join(symbols),
            "range":range,
            "interval":interval,
            "corsDomain": "finance.yahoo.com",
            "fields": "exchangeTimezoneName,regularMarketTime,marketCap, exchangeName"
        }
        res = requests.get(
            url=self.base_url + "v7/finance/quote", 
            params=params,
            headers=headers,
            proxies=self.format_proxy()
        )
        res_data = json.loads(res.text).get("quoteResponse", {}).get("result", [])
        if len(symbols) > 1:
            stock_response_classes = []
            for stock in res_data:
                stock_dataclass = Stock(stock)
                stock_response_classes.append(stock_dataclass)
            return stock_response_classes
        else:
            stock_dataclass = Stock(res_data[0])
            return stock_dataclass


        
        