import requests
from pprint import pprint


def main():
    data = api_call()
    exchange_rate = get_exchange_value(data)
    bitcoin_values = convert_to_bitcoin(exchange_rate)
    print_bitcoin(bitcoin_values)


def api_call():
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(coindesk_url)
    data = response.json()
    
    return data

def get_exchange_value(data):
    dollars_exchange_rate = data['bpi']['USD']['rate_float']
    print(dollars_exchange_rate)
    return dollars_exchange_rate

def convert_to_bitcoin(dollars_exchange_rate):
    bitcoin = 1
    bitcoin_value = bitcoin * dollars_exchange_rate
    return bitcoin_value

def print_bitcoin(bitcoin_value):
    bitcoin = 1
    print (f'{bitcoin} Bitcoin is equal to {bitcoin_value} dollars')



if __name__ == '__main__':
    main()
