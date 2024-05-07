# coding: utf-8

def build_dict(elms=[]):
    # 与えられた要素パスを元に、辞書を作成する

    KEY_IDX = 0
    VALUE_IDX = 1
    TYPE_IDX = 2

    LIST_LABEL = 'l'
    DICT_LABEL = 'd'

    # 要素パスを元に、辞書ツリーを作成する
    if elms[0][TYPE_IDX] == LIST_LABEL:
        # パスの先頭要素がリストの場合
        if elms[0][VALUE_IDX] == []:
            return []
        else:
            if len(elms) > 1:
                return build_dict(elms[1:])
            else:
                return elms[0][VALUE_IDX]
    elif elms[0][TYPE_IDX] == DICT_LABEL:
        # パスの先頭要素が辞書の場合
        if elms[0][VALUE_IDX] == {}:
            return {}
        else:
            if len(elms) > 1:
                return {elms[0][KEY_IDX]: build_dict(elms[1:])}
            else:
                return {elms[0][KEY_IDX]: elms[0][VALUE_IDX]}
    else:
        return elms[0]