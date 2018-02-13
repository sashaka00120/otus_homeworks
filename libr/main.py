import os
import collections

from libr.handler import get_top_verbs_in_path
from libr.projects import projects
from libr.logger import *



if __name__ == "__main__":
    final_list = []

    for project in projects:
        path = os.path.join('../..', project)
        format_logging_info('Start project: '+ project)
        final_list += get_top_verbs_in_path(path)

    top_size = 200
    print('total %s words, %s unique' % (len(final_list), len(set(final_list))))

    for word, occurence in collections.Counter(final_list).most_common(top_size):
        print(word, occurence)

    format_logging_info('Finish')