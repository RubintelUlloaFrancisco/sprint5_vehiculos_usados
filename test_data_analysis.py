import unittest
from data_analysis import load_data, plot_data, validate_file
import pandas as pd

class TestDataAnalysis(unittest.TestCase):

    def test_validate_file(self):
        self.assertTrue(validate_file('test_data.csv'))
        self.assertFalse(validate_file('non_existent.csv'))

    def test_load_data(self):
        data = load_data('test_data.csv')
        self.assertIsInstance(data, pd.DataFrame)

    def test_plot_data(self):
        data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
        try:
            plot_data(data, 'col1', 'col2')
        except Exception as e:
            self.fail(f"plot_data() raised Exception unexpectedly: {e}")

if __name__ == '__main__':
    unittest.main()

