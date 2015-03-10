import unittest
import yaml

# should test that calendar dates are all strings
# should test that calendar date strings are all XXXX-XX-XX
# should test calendar entries are in order, makes human edits easier
# should test other calendar properties


class TestData(unittest.TestCase):
    def setUp(self):
        data_files = [
            'calendar'
        ]

        self.data = {}
        for data_current in data_files:
            with open('_data/{}.yml'.format(data_current)) as f:
                self.data[data_current] = yaml.load(f)

    def test_parse_yaml(self):
        pass

