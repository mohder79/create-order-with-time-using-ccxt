import ccxt
from pprint import pprint
import time
import api_config as ac

exchange = ccxt.kucoinfutures({
    'adjustForTimeDifference': True,
    'apiKey': ac.API_KEY,
    'secret': ac.SECRET_KEY,
    'password': ac.PASSWORD,
})


markets = exchange.load_markets()
print(exchange)


symbol = 'LUNA/USDT:USDT'
amount = 3000
price = 0.0001
type = 'limit'

run = True
sleep_time = 20


while run == True:
    pprint('bot is working')

    order = exchange.create_limit_buy_order(
        symbol, amount, price)
    pprint(order)

    pprint(f'i made your order now i sleep for {sleep_time} seconds')
    time.sleep(sleep_time)
