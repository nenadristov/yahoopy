from YahooPy.yahoopy import Client
cl= Client()

res = cl.get_stock(symbols=["aapl", "MSFT"], interval="5m")
print(res[0].to_json())