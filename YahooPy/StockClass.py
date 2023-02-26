from dataclasses import dataclass

@dataclass
class Stock:


    def __init__(self, raw_data:dict) -> None:
        self.currency = raw_data.get("currency", None)
        self.symbol = raw_data.get("symbol", None)
        self.exchange_name = raw_data.get("fullExchangeName", None)
        self.firts_trade_date_time = raw_data.get("firstTradeDateMilliseconds", None)
        self.reguler_market_time = raw_data.get("regularMarketTime", None)
        self.timezone = raw_data.get("exchangeTimezoneShortName", None)
        self.market_price = raw_data.get("regularMarketPrice", None)
        self.market_cap = raw_data.get("marketCap", None)
        self.market_state = raw_data.get("marketState", None)
        self.crypto_tradable = raw_data.get("cryptoTradeable", None)


    def to_json(self):
        data = {
            "currency":self.currency,
            "symbol":self.symbol,
            "exchange_name":self.exchange_name,
            "firts_trade_date_time":self.firts_trade_date_time,
            "reguler_market_time":self.reguler_market_time,
            "timezone":self.timezone,
            "market_price":self.market_price,
            "market_cap":self.market_cap,
            "market_state":self.market_state,
            "crypto_tradable":self.crypto_tradable

        }

        return data
        

        
