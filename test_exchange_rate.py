import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import patch


import exchange_rate


class TestExchangeRates(TestCase):

    @patch('exchange_rate.request_rates')
    def test_dollars_to_target(self, mock_rates):
        mock_rate =123.4567
        #must be exact
        example_api_resonse = {"rates":{"CAD":mock_rate}, "base":"USD", "date":"2020-10-02"}
        mock_rates.side_effect = [ example_api_resonse ]
        converted = exchange_rate.convert_dollars_to_target(100, 'CAD')
        expected = 12345.67
        self.assertEqual(expected, converted)

    @patch('requests.get')
    def test_dollars_to_target_2(self, mock_requests_get):
        mock_rate = 123.4567
        example_api_response = {"rates":{"CAD":mock_rate}, "base":"USD", "date":"2020-10-02"}
        mock_requests_get().json.return_value = example_api_response
        converted = exchange_rate.convert_dollars_to_target(100, 'CAD')
        expected = 12345.67
        self.assertEqual(expected, converted)