# coding: utf-8

import sys

from yield_dict_path_elms import yield_dict_path_elms
from merge_dict_elms import merge_dict_elms

def split_dict(dic={}, split_size=1024):
    # 入力された辞書を、指定サイズ以下の辞書に分割する

    VALUE_IDX = 1

    new_dic = {}
    size = 0
    for elms in yield_dict_path_elms(dic):
        size += sys.getsizeof(elms[-1][VALUE_IDX])

        if size > split_size:
            yield new_dic
            new_dic = {}
            size = 0

        new_dic = merge_dict_elms(new_dic, elms)
        
    yield new_dic