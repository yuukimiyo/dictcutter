import unittest

import sys
from pathlib import Path
sys.path.append(str(Path(Path(__file__).parent / '../src/dictcutter').resolve()))
from build_dict import build_dict


class TestBuildDict(unittest.TestCase):

    def test_build_dict(self):
        elms = [('key1', '', 'd'), (0, '', 'l'), ('key1-1', 'key1-1v', 'd')]
        expected = {'key1': {'key1-1': 'key1-1v'}}
        actual = build_dict(elms)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
