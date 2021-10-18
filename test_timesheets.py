import unittest
from unittest import TestCase
from unittest.mock import patch, call

import timesheets

class TestTimesheet(TestCase):
    """ mock input and force it to return a value"""

    @patch('builtins.input', side_effect=['2'])
    # @patch creates a mock object for builtins.input creates object
    # if you call input it asks for input, this puts input in instead
    #of asking for input, side_effect is the return value it needs to be a list
    # side_effects are iterable like a list

    # to return the same value @patch('builtins.input', return_value='bob')
    
    def test_get_hours_for_day(self, mock_input):
        # you need mock_input to work
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2, hours)

    @patch('builtins.input', side_effect=['cat', '', 'fish', '123bird','pizza1234', '2'])
    # side_effect calls first thing in list the first time its run the second thing in
    #list the second time it's run ect..
    # test won't quit until a valid value is returned so you need to end with a valid value
    def test_get_hours_for_day_non_numeric_rejected(self, mock_input):
        # you need mock_input to work
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2, hours)

   


    @patch('builtins.input', side_effect=['25', '24.0001' '100', '-2', '2'])
    def test_get_hours_wont_work_with_a_number_over_24(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2, hours)
        # make different tests for negative and over 24

    @patch('builtins.print')
    # no side_effect needed because nothing is being returned
    def test_display_total(self, mock_print):
        timesheets.display_total(123)
        mock_print.assert_called_once_with('Total hours worked: 123')
        #tests what would be printed


    @patch('timesheets.alert')
    # timesheets.alert is function to test
    def test_alert_meet_min_hours_doesnt_meet(self, mock_alert):
        timesheets.alert_not_meet_min_hours(12, 30)
        mock_alert.assert_called_once()

    @patch('timesheets.alert')
    def test_alert_meet_min_hours_exceed(self, mock_alert):
        timesheets.alert_not_meet_min_hours(45, 30)
        mock_alert.assert_not_called()
    
    # a mock function

    @patch('timesheets.get_hours_for_day')
    def test_get_hours(self, mock_get_hours):
        mock_hours = [5, 6, 7]
        # if you use data in a variable you have to set side effect
        # if you return something you need a side_effect
        mock_get_hours.side_effect = mock_hours
        days = ['m', 't', 'w'] 
        # makes a dictionary from 2 lists
        expected_hours = dict(zip(days, mock_hours))
        hours = timesheets.get_hours(days)
        self.assertEqual(expected_hours, hours)

    # @patch('builtins.print')
    # def test_display_hours(self, mock_print):
    #     example = {'m': 3, 't': 12, 'w': 8.5}
    #     # when a mock is called it creates a call object which stores data in a tuple
        
    #     # this must be exatly as it's printed
    #     expected_table_calls = [
    #         call('Day          Hours worked   '),           
    #         call('m              3            '),
    #         call('t              12           '),
    #         call('w              8.5          '),
    #     ]
    #     timesheets.display_hours(example)
    #     mock_print.assert_has_calls(expected_table_calls)

    def test_total_hours_(self):
        example = {'m': 3, 't': 12, 'w': 8.5}
        total = timesheets.total_hours(example)
        expected_total = 3 + 12 + 8.5
        self.assertEqual(total, expected_total)





if __name__ == '__main__':
    unittest.main()
