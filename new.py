import ast
import os
import collections

from nltk import pos_tag


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'


def get_filenames(path):

    path = Path
    filenames = []

    for dirname, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.endswith('.py') and len(filenames) < 100:
                filenames.append(os.path.join(dirname, file))
    print('total %s files' % len(filenames))
    return filenames

def get_trees(path):
    trees=[]
    for filename in get_filenames(path):
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            print(e)
            tree = None
        trees.append(tree)
    print('trees generated')
    return trees








def get_all_names(tree):
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]

def is_two_split(f):
    trees = [t for t in get_trees(None) if t]
    return f.startswith('__') and f.endswith('__')

def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def get_all_words_in_path(path):
    trees = [t for t in get_trees(path) if t]
    function_names = [f for f in flat([get_all_names(t) for t in trees]) if not is_two_split(f)]

    def split_snake_case_name_to_words(name):
        return [n for n in name.split('_') if n]

    return flat([split_snake_case_name_to_words(function_name) for function_name in function_names])


def names_from_trees_without_standard_names():
    fncs = [f for f in get_names_from_trees() if not is_two_split(f)]
    print(fncs)
    return fncs

def get_names_from_trees():
    trees = [t for t in get_trees(None) if t]
    return flat([[node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)] for t in trees])


def get_top_verbs_in_path(path, top_size=10):
    global Path
    Path = path
    verbs = flat([get_verbs_from_function_name(function_name) for function_name in names_from_trees_without_standard_names()])
    return collections.Counter(verbs).most_common(top_size)

def get_top_functions_names_in_path(path, top_size=10):
    return collections.Counter(names_from_trees_without_standard_names()).most_common(top_size)

wds = []
projects = [
    'dz1',
    'nicecash',
    'blog',
    'untitled',
    'untitled1',
    'untitled5',
]
for project in projects:
    path = os.path.join('..', project)
    wds += get_top_verbs_in_path(path)
    print(get_all_words_in_path(path))

top_size = 200
print('total %s words, %s unique' % (len(wds), len(set(wds))))
for word, occurence in collections.Counter(wds).most_common(top_size):
    print(word, occurence)