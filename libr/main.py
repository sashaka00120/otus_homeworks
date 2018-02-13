import os
import collections

from libr.handler import get_top_verbs_in_path
from libr.projects import projects
from libr.logger import *



if __name__ == "__main__":
    wds = []
    pls = []


    for project in projects:
        path = os.path.join('../..', project)
        format_logging_info('Start project: '+ project)
        wds += get_top_verbs_in_path(path)

    top_size = 200
    print('total %s words, %s unique' % (len(wds), len(set(wds))))
    for word, occurence in collections.Counter(wds).most_common(top_size):
        print(word, occurence)
    format_logging_info('Finish')