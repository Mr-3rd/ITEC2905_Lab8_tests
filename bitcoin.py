import requests 

def main():
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    data = get_exchange_rate(coindesk_url)

    bitcoin = get_bitcoins()

    euro_exchange_rate = convert_bitcoin_to_euro(data)

    bitcoin_value_in_dollars = bitcoin * euro_exchange_rate

    print(f'{bitcoin} Bitcoin is equivalent to ${bitcoin_value_in_dollars}')


def get_exchange_rate(coindesk_url):
    response = requests.get(coindesk_url)

    data = response.json()
    # pprint(data)

    return data


def get_bitcoins():
    bitcoin = input('Enter the number of bitcoin: ')

    while bitcoin.isnumeric is False:
        bitcoin = input('Enter a number of bitcoin: ')
    
    bitcoin = float(bitcoin)

    while bitcoin <= 1:
        bitcoin = input('Enter a positive number of bitcoin: ')

    return float(bitcoin)

def convert_bitcoin_to_euro(data):
    euro_exchange_rate = data['bpi']['EUR']['rate_float']
    return euro_exchange_rate


# without this, the tests will call main when this file is imported
if __name__ == '__main__':
    main()