import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dictcutter')))

import dictcutter

class TestYieldDictPathElms(unittest.TestCase):

    def test_yield_dict_path_elms(self):
        dict = {'key1': {'key1-1': 'key1-1v'}}
        actual = None
        for elms in dictcutter.yield_dict_path_elms(dict):
            actual = elms
            break
        expected = [('key1', '', 'd'), ('key1-1', 'key1-1v', 'd')]
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
