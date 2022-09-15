import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://www.coingecko.com/')
soup = BeautifulSoup(response.content, 'html.parser')
coin_name = soup.find_all('div', attrs={'class':'tw-flex-auto'})
coin_list = []
coin_price_list = []
a_day_volume_list = []
market_cap_list = []
for i in coin_name:
    span_tag = i.find('span', attrs={'class':'lg:tw-flex font-bold tw-items-center tw-justify-between'}).text
    coin = span_tag.strip()
    coin_list.append(coin+',')

coin_price_div_tag = soup.find_all('div', attrs={'class':'tw-flex tw-justify-between tw-items-center tw-gap-2'})
for p in coin_price_div_tag:
    coin_price = p.find('span').text.replace(',', '')
    coin_price_list.append(coin_price+',')

volume_td_tag = soup.find_all('td', attrs={'class':'td-liquidity_score lit text-right col-market'})
for v in volume_td_tag:
    volume = v.find('span').text.replace(',', '')
    a_day_volume_list.append(volume+',')

market_cap_td_tag = soup.find_all('td', attrs={'class':'td-market_cap cap col-market cap-price text-right'})
for m in market_cap_td_tag:
    market = m.find('span').text.replace(',', '')
    market_cap_list.append(market+',')

data = {
    'Coin Name,': coin_list,
    'Coin Price,': coin_price_list,
    '24h Volume,': a_day_volume_list,
    'Market Cap,': market_cap_list
}
row_data = pd.DataFrame(data)
row_data.to_csv('market_data.csv', sep='\t', index=False)
print(row_data)
