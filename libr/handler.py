import ast
import collections

from libr.trees import get_trees
from nltk import pos_tag
from libr.logger import *


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] is 'VB' or 'VD' or 'VN'


def get_all_names(tree):
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def is_start_end(f):
    return f.startswith('__') and f.endswith('__')


def get_all_words_in_path(path, top_size=10):
    trees = [t for t in get_trees(path) if t]
    function_names = [f for f in flat([get_all_names(t) for t in trees]) if not is_start_end(f)]
    def split_snake_case_name_to_words(name):
        return [n for n in name.split('_') if n]
    verbs2 = flat([split_snake_case_name_to_words(function_name) for function_name in function_names])
    return collections.Counter(verbs2).most_common(top_size)


def get_top_verbs_in_path(path, top_size=10):
    trees = [t for t in get_trees(path) if t]
    fncs = [f for f in
            flat([[node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)] for t in trees]) if
            not is_start_end(f)]
    format_logging_debug('functions extracted')
    verbs = flat([get_verbs_from_function_name(function_name) for function_name in fncs])
    top_verbs =collections.Counter(verbs).most_common(top_size)
    format_logging_info(top_verbs)
    return top_verbs



