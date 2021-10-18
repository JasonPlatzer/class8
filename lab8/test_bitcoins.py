import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import patch, call


import bitcoins


class TestBitcoins(TestCase):

    # creating a mock api call
    @patch('bitcoins.api_call')
    def test_get_exchange_value(self, mock_rate):
        # different bitcoin values because it was something different each time I checked the value
        exchange_rate = 56882.7417
        # a fake result of an api call
        example_api_response = {'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': exchange_rate, 'description': 'United States Dollar', 'rate_float': 56882.7417}}}
        # setting the value of what would be put into the function if it was run in main program
        mock_rate.side_effect = [example_api_response]
        # testing the function
        value_of_one_bitcoin = bitcoins.get_exchange_value(example_api_response)
        # checking if the value of what should result when function runs with what actuall results when function is run
        self.assertEqual(exchange_rate, value_of_one_bitcoin)

    @patch('bitcoins.get_exchange_value')
    def test_convert_to_bitcoin(self, mock_rate):
        # the exchange rate of bitcoin when function was made
        exchange_rate = 55024.18
        # 1 is the value I set program to so it wouldn't need user input
        exchange_value = 1 * exchange_rate
        # calling the function on value of what would be put in if run in main program
        converted = bitcoins.convert_to_bitcoin(exchange_value)
        self.assertEqual(exchange_value, converted)

    @patch('builtins.print')
    def test_print_bitcoin(self, mock_print):
        bitcoin_value = 55024.18
        bitcoins.print_bitcoin(bitcoin_value)
        # what should be printed
        example = [f'1 Bitcoin is equal to {bitcoin_value} dollars']
        #seeing if there is a call for what should be printed
        mock_print.assert_has_calls(example)



    