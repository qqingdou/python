# -*- coding: utf-8 -*-
# win 7
#author : 442353346@qq.com
#desc: if you find your disk always has no space, you can use it to find big file

import sys
import os
import threading

BIG_FILE_MIN = 10 * 1024 * 1024
BIG_FILES_LIST = []

def __main__():
    dir_path = raw_input('please input search path:')
    if dir_path is None or not os.path.isdir(dir_path):
        print 'please input valid dir.'
        sys.exit()

    #prevent first dir too many files or dirs
    my_thread = threading.Thread(target=get_main_dir, args=(dir_path,))
    my_thread.start()

def get_main_dir( dir ):

    global BIG_FILES_LIST

    try:

        lists = os.listdir( dir )
        first_dirs = []

        if lists is not None and len(lists) > 0:
            for item in lists:
                path = '%s%s%s' % (dir, (dir.endswith('\\') and ' ' or '\\').strip(), item)
                if os.path.isdir(path):
                    first_dirs.append( path )
                elif os.path.isfile( path ):
                    file_size = os.path.getsize( path )
                    if file_size >= BIG_FILE_MIN:
                        BIG_FILES_LIST.append({'path': path, 'size': file_size})
                        #print unicode('file path : %s, file size: %s MB' % (path, file_size / 1024 / 1024), 'gbk')

        if len(first_dirs) > 0:
            for item in first_dirs:
                my_thread = threading.Thread(target=find_big_file, args=(item,))
                my_thread.start()

    except:
        pass

def find_big_file( dir ):

    global BIG_FILE_MIN

    try:
        if os.path.isdir( dir ):
            #get dir contents
            lists = os.listdir( dir )

            if lists is not None and len(lists) > 0:
                for item in lists:
                    path = '%s%s%s' % (dir,(dir.endswith('\\') and ' ' or '\\').strip() ,item)
                    if os.path.isdir(path):
                        find_big_file(path)
                    elif os.path.isfile( path ):
                        file_size = os.path.getsize(path)
                        if file_size >= BIG_FILE_MIN:
                            print unicode('file path : %s, file size: %s MB' % (path, file_size / 1024 / 1024), 'gbk')

    except:
        pass

if __name__ == '__main__':
    __main__()