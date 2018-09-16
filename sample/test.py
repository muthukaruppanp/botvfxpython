#!/usr/bin/env python
import os
from collections import defaultdict

def breathfirstsearch( root ) :
	dirs = [root]
	while len(dirs) :
		nextDirs = []
		for parent in dirs :
			for f in os.listdir( parent ) :
				ff = os.path.join( parent, f )

				if os.path.isdir( ff ) :
					nextDirs.append( ff )
				else :
					yield ff
		dirs = nextDirs
		
# refered from https://stackoverflow.com/questions/8484943/construct-a-tree-from-list-os-file-paths-python-performance-dependent
FILE_MARKER = '<files>'

def attach(branch, trunk):
    '''
    Insert a branch of directories on its trunk.
    '''
    parts = branch.split('/', 1)
    if len(parts) == 1:
        trunk[FILE_MARKER].append(parts[0])
    else:
        node, others = parts
        if node not in trunk:
            trunk[node] = defaultdict(dict, ((FILE_MARKER, []),))
        attach(others, trunk[node])

def prettify(d, indent=0):
    '''
    Print the file tree structure with proper indentation.
    '''
    for key, value in d.iteritems():
        if key == FILE_MARKER:
            if value:
				for i in value:
					print ' ' *4* indent +str(i)
        else:
            print ' '*4* indent + str(key)
            if isinstance(value, dict):
                prettify(value, indent+1)
            else:
                print ' '*4* (indent+1) + str(value)


if __name__ == "__main__":
	main_dict = defaultdict(dict, ((FILE_MARKER, []),))
	for f in breathfirstsearch(os.getcwd()) :
		attach(f, main_dict)

	prettify(main_dict)
