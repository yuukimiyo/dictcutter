# coding: utf-8

def yield_dict_path_elms(obj, path=[]):
    # 与えられたオブジェクトの各要素について、要素パスオブジェクト(※)をyieldする
    # ※要素パスオブジェクト：(key, value, type)のタプルのリスト

    LIST_LABEL = 'l'
    DICT_LABEL = 'd'

    if isinstance(obj, dict):
        # 入力の1次元目が辞書の場合
        if obj == {}:
            yield path + [('', {}, 'd')]
        else:
            for key, value in obj.items():
                if isinstance(value, dict):
                    # 小要素ツリーを作成し元の辞書に追加
                    yield from yield_dict_path_elms(value, path + [(key, '', DICT_LABEL)])
                elif isinstance(value, (list, tuple)):
                    # 小要素ツリーを作成し元の辞書に追加
                    yield from yield_dict_path_elms(value, path + [(key, '', DICT_LABEL)])
                else:
                    # 通常の変数（ツリーの末端）の場合
                    yield path + [(key, value, DICT_LABEL)]
    elif isinstance(obj, (list, tuple)):
        # 入力の1次元目がリストの場合
        if obj == []:
            yield path + [('', [], LIST_LABEL)]
        else:
            for i, value in enumerate(obj):
                if isinstance(value, dict):
                    # 辞書か配列の、小要素ツリーを作成し元のリストに追加
                    yield from yield_dict_path_elms(value, path + [(i,'', LIST_LABEL)])
                elif isinstance(value, (list, tuple)):
                    # 辞書か配列の、小要素ツリーを作成し元のリストに追加
                    yield from yield_dict_path_elms(value, path + [(i,'', LIST_LABEL)])
                else:
                    # 通常の変数（ツリーの末端）の場合
                    yield path + [(i, value, LIST_LABEL)]
    else:
        # 入力の1次元目が通常の変数の場合
        yield [('', obj, '')]