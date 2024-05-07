import unittest

import sys
from pathlib import Path
sys.path.append(str(Path(Path(__file__).parent / '../src/dictcutter').resolve()))
from merge_dict_elms import merge_dict_elms

class TestMergeDictElms(unittest.TestCase):

    def test_merge_value(self):
        # 辞書への追加（配列化＋変数をアペンド）
        dict1 = {'key1': {'key1-1': 'key1-1v'}}
        dict2_elms = [('key1', 'key1v', 'd')]
        expected = {'key1': [{'key1-1': 'key1-1v'}, 'key1v']}
        actual = merge_dict_elms(dict1, dict2_elms)
        self.assertEqual(expected, actual)

    def test_merge_multikeydict(self):
        # 辞書への追加（key-valueペア追加）
        dict1 = {'key1': {'key1-1': 'key1-1v'}}
        dict2_elms = [('key1', '', 'd'), (0, '', 'l'), ('key1-2', 'key1-2v', 'd')]
        expected = {'key1': {'key1-1': 'key1-1v', 'key1-2': 'key1-2v'}}
        actual = merge_dict_elms(dict1, dict2_elms)
        self.assertEqual(expected, actual)

    def test_merge_multidict(self):
        # 辞書への追加（配列化＋辞書をアペンド）
        dict1 = {'key1': {'key1-1': 'key1-1v'}}
        dict2_elms = [('key1', '', 'd'), (1, '', 'l'), ('key1-2', 'key1-2v', 'd')]
        expected = {'key1': [{'key1-1': 'key1-1v'}, {'key1-2': 'key1-2v'}]}
        actual = merge_dict_elms(dict1, dict2_elms)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
