# coding: utf-8

from build_dict import build_dict

def merge_dict_elms(left, elms=[], prev_list_index=0):
    KEY_IDX = 0
    VALUE_IDX = 1
    TYPE_IDX = 2

    LIST_LABEL = 'l'
    DICT_LABEL = 'd'

    if isinstance(left, (list, tuple)):
        # マージ対象がリストの場合
        r = left[:]
        if elms[0][TYPE_IDX] == LIST_LABEL:
            list_index = elms[0][KEY_IDX]
            if len(r) > list_index:
                r[list_index] = merge_dict_elms(r[list_index], elms[1:], list_index)
            else:
                r.append(build_dict(elms[1:]))
            return r
        r.append(build_dict(elms[1:]))
        return r
    elif hasattr(left, "get"):
        # マージ対象が辞書の場合
        r = left.copy()
        if elms[0][TYPE_IDX] == DICT_LABEL:
            k = elms[0][KEY_IDX]
            if k in r:
                if len(elms) == 1:
                    print([r[k], elms[0][VALUE_IDX]])
                    r[k] = [r[k], elms[0][VALUE_IDX]]
                else:
                    r[k] = merge_dict_elms(r[k], elms[1:], 0)
            else:
                if len(elms) == 1:
                    r[k] = elms[0][VALUE_IDX]
                else:
                    r[k] = build_dict(elms[1:])

            return r
        elif elms[0][TYPE_IDX] == LIST_LABEL:
            list_index = elms[0][KEY_IDX]

            if len(elms) > 0 and elms[1][TYPE_IDX] == DICT_LABEL:
                # elmsにおいて、配列の直下が辞書の場合、一つの辞書に複数のkey-valueペアが存在する場合（例：{'k1': 'v1', 'k2': 'v2'}）と、単一のkey-value辞書による配列の場合に処理を分け、
                # 前者の場合はleftの辞書に統合する処理を行う。
                k = elms[1][KEY_IDX]
                if k in r:
                    if list_index <= prev_list_index:
                        # 一つの辞書に複数のkey-valueペアが存在する場合（例：{'k1': 'v1', 'k2': 'v2'}）
                        if len(elms) == 2:
                            r[k] = [r[k], elms[1][VALUE_IDX]]
                        else:
                            r[k] = merge_dict_elms(r[k], elms[2:], list_index)
                        return r
                else:
                    if list_index <= prev_list_index:
                        # 一つの辞書に複数のkey-valueペアが存在する場合（例：{'k1': 'v1', 'k2': 'v2'}）
                        if len(elms) == 2:
                            r[k] = elms[1][VALUE_IDX]
                        else:
                            r[k] = build_dict(elms[2:])
                        return r
            
            # （それ以外）単一のkey-valueペアによる配列（例：[{'k1': 'v1'}, {'k2': 'v2'}]）
            return [r, build_dict(elms)]
        else:
            return [r, elms[0][VALUE_IDX]]
    else:
        return [left, build_dict(elms)]
