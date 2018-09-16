#!/usr/bin/env python
import os
from collections import defaultdict
class Breathfirstsearch:

    """docstring for Breathfirstsearch."""

    def __init__(self,dir_name):
        self.path = dir_name
        self.FILE_MARKER = '<files>'

    def breathfirstsearch(self) :
    	dirs = [self.path]
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

    def attach(self,branch, trunk):
        '''
        Insert a branch of directories on its trunk.
        '''
        parts = branch.split('/', 1)
        if len(parts) == 1:
            trunk[self.FILE_MARKER].append(parts[0])
        else:
            node, others = parts
            if node not in trunk:
                trunk[node] = defaultdict(dict, ((self.FILE_MARKER, []),))
            self.attach(others, trunk[node])

    def prettify(self,d, indent=0):
        '''
        Print the file tree structure with proper indentation.
        '''
        for key, value in d.iteritems():
            if key == self.FILE_MARKER:
                if value:
    				for i in value:
    					print ' ' *4* indent +str(i)
            else:
                print ' '*4* indent + str(key)+'/'
                if isinstance(value, dict):
                    self.prettify(value, indent+1)
                else:
                    print ' '*4* (indent+1) + str(value)

if __name__ == "__main__":

    dir_name = os.getcwd()+'/sample/'
    bfs = Breathfirstsearch(dir_name)
    bfs.breathfirstsearch()
    main_dict = defaultdict(dict, ((bfs.FILE_MARKER, []),))
    for f in bfs.breathfirstsearch() :
        bfs.attach(f, main_dict)

    bfs.prettify(main_dict)
