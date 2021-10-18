import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = widget('the widget')

    def tearDown(self):
        self.widget.dispose()