import os
import ast

from libr.logger import *


def get_filenames(path):

    filenames = []

    for dirname, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.endswith('.py') and len(filenames) < 100:
                filenames.append(os.path.join(dirname, file))
    return filenames

def get_trees(path):
    trees=[]
    for filename in get_filenames(path):
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            format_logging_debug('open file in path is OK')
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            format_logging_error('SyntaxError in func get_trees, tree = None')
            tree = None
        trees.append(tree)
    return trees

