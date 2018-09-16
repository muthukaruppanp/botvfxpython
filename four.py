#!/usr/bin/env python
import os
from collections import defaultdict
def depthfirstsearch(dir_name, visited = [], results = [],tabspace = 0):
    dirs = os.listdir(dir_name)
    if dirs:
        for f in dirs:
            new_dir = dir_name + f + '/'
            if os.path.isdir(new_dir) and new_dir not in visited:
                # print(tabspace*4*' '+f+'/')
                # tabspace +=1
                visited.append(new_dir)
                depthfirstsearch(new_dir, visited, results,tabspace)
            else:
                results.append(dir_name+f)
                # tabspace +=1
                # print(tabspace*4*' '+f)
            # tabspace -=1
    return results

def attach(branch, trunk):
    parts = branch.split('/', 1)
    if len(parts) == 1:
        trunk[FILE_MARKER].append(parts[0])
    else:
        node, others = parts
        if node not in trunk:
            trunk[node] = defaultdict(dict, ((FILE_MARKER, []),))
        attach(others, trunk[node])

def prettify(d, indent=0):
    for key, value in d.iteritems():
        if key == FILE_MARKER:
            if value:
                for i in value:
                    print ' '*4* indent +str(i)
        else:
            print ' '*4* indent + str(key)+'/'
            if isinstance(value, dict):
                prettify(value, indent+1)
            else:
                print ' '*4* (indent+1) + str(value)

dir_name = os.getcwd()+'/sample/'
FILE_MARKER = '<files>'
main_dict = defaultdict(dict, ((FILE_MARKER, []),))
for f in depthfirstsearch(dir_name) :
    attach(f, main_dict)

prettify(main_dict)
