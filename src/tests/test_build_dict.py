import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dictcutter')))

import dictcutter

class TestBuildDict(unittest.TestCase):

    def test_build_dict(self):
        elms = [('key1', '', 'd'), (0, '', 'l'), ('key1-1', 'key1-1v', 'd')]
        expected = {'key1': {'key1-1': 'key1-1v'}}
        actual = dictcutter.build_dict(elms)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
