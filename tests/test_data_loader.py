import unittest
from unittest.mock import patch
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from data_loader import load_raw_data, save_processed_data

class TestDataLoader(unittest.TestCase):
    @patch('data_loader.pd.read_csv')
    def test_load_raw_data(self, mock_read_csv):
        """Teste le chargement des données brutes en mockant pandas.read_csv"""
        mock_df = pd.DataFrame({'col1': [1, 2]})
        mock_read_csv.return_value = mock_df
        
        file_name = "test.csv"
        df = load_raw_data(file_name)
        
        expected_path = os.path.join('data', 'raw', file_name)
        mock_read_csv.assert_called_once_with(expected_path)
        pd.testing.assert_frame_equal(df, mock_df)

    @patch('data_loader.pd.DataFrame.to_csv')
    def test_save_processed_data(self, mock_to_csv):
        """Teste la sauvegarde des données traitées en mockant pandas.to_csv"""
        df = pd.DataFrame({'col1': [1, 2]})
        file_name = "test_processed.csv"
        
        save_processed_data(df, file_name)
        
        expected_path = os.path.join('data', 'processed', file_name)
        mock_to_csv.assert_called_once_with(expected_path, index=False)

if __name__ == '__main__':
    unittest.main()
