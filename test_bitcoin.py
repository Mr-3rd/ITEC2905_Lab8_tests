import unittest 
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin

class TestBitcoin(TestCase):
    @patch('bitcoin.get_exchange_rate')
    def test_get_exchange_rate(self, mock_bitcoin_call):
        mock_bitcoin_call.return_value = {'bpi': 
                    {'EUR': {'code': 'EUR', 'description': 'Euro',
                             'rate': '26,112.5741','rate_float': 26112.5741, 
                             'symbol': '&euro;'},
                    'GBP': {'code': 'GBP',
                 'description': 'British Pound Sterling',
                 'rate': '22,398.5501',
                 'rate_float': 22398.5501,
                 'symbol': '&pound;'},
                 'USD': {'code': 'USD',
                 'description': 'United States Dollar',  
                 'rate': '26,805.6063',
                 'rate_float': 26805.6063,
                 'symbol': '&#36;'}},
                 'chartName': 'Bitcoin',
                 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index '
               '(USD). Non-USD currency data converted using hourly conversion '
               'rate from openexchangerates.org',
               'time': {'updated': 'Oct 12, 2023 00:55:00 UTC',
                        'updatedISO': '2023-10-12T00:55:00+00:00',
                        'updateduk': 'Oct 12, 2023 at 01:55 BST'}
                        }
        
        expected_output = 26112.5741

        euro = bitcoin.convert_bitcoin_to_euro(mock_bitcoin_call)


        self.assertEqual(expected_output, euro)
