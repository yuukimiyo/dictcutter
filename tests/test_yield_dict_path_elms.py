import unittest

import sys
from pathlib import Path
sys.path.append(str(Path(Path(__file__).parent / '../src/dictcutter').resolve()))
from yield_dict_path_elms import yield_dict_path_elms


class TestYieldDictPathElms(unittest.TestCase):

    def test_yield_dict_path_elms(self):
        dict = {'key1': {'key1-1': 'key1-1v'}}
        actual = None
        for elms in yield_dict_path_elms(dict):
            actual = elms
            break
        expected = [('key1', '', 'd'), ('key1-1', 'key1-1v', 'd')]
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
