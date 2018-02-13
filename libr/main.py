import os
import collections

from libr.handler import get_top_verbs_in_path
from libr.projects import projects


if __name__ == "__main__":
    wds = []
    pls = []


    for project in projects:
        path = os.path.join('../..', project)
        wds += get_top_verbs_in_path(path)

    top_size = 200
    print('total %s words, %s unique' % (len(wds), len(set(wds))))
    for word, occurence in collections.Counter(wds).most_common(top_size):
        print(word, occurence)