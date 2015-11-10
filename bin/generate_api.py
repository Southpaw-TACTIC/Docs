#!/usr/bin/python 
###########################################################
#
# Copyright (c) 2005, Southpaw Technology
#                     All Rights Reserved
#
# PROPRIETARY INFORMATION.  This software is proprietary to
# Southpaw Technology, and is not to be reproduced, transmitted,
# or disclosed in any way without written permission.
#
#
#


__all__ = ['GenerateApiDoc']

import tacticenv
from tactic_client_lib import TacticServerStub

import unittest
import xmlrpclib, sys, os, shutil
import re

class GenerateApiDoc(object):


    def execute(my):
        path = 'tactic_server_stub.py'
        f = open(path, 'r')
        lines = f.readlines()
        started = False
        param_started = False
        doc_str = []
        short_title = None
        count = 0
        my.final_func_paths = []
        my.final_paths = []
        plain_function = False
        
        strip = True
        for line in lines:
            if strip:
                line = line.strip()
                #print "strip ", line
            if line.startswith("'''API Function") or line.startswith("'''Function") :
                count += 1
                if line.startswith("'''Function"):
                    plain_function = True
                    title = line.replace("'''Function:", '').strip()
                else:
                    title = line.replace("'''API Function:", '').strip()
                short_title = title.split('(')[0]
                slash = False

                # detect it's a slash
                if short_title.startswith('__'):
                    short_title = '\\\\%s'%short_title
                    title = '\\\\%s'%title
                    
                    slash = True

                doc_str.append(short_title)
                doc_str.append('-'* len(short_title))
                doc_str.append('')
                doc_str.append('*%s*'%title)
                doc_str.append('')
                #doc_str.append(line)
                
                started = True
                continue

            if started:
                # subtitle
                if line.startswith('@'):
                    line = line.replace('@','*')
                    line = '%s*' %line
                    param_started = True
                    doc_str.append(line)
                    doc_str.append('')
                    continue
                if param_started:
                    line = re.sub(r'(.*) - (.*)',r'*\g<1>* - \g<2>', line)
                

                if line.startswith('[code]') or line.find('[/code]') != -1 :

                    if line.startswith('[code]'):
                        doc_str.append('[source,python]')
                        strip = False
                    else:
                        strip = True

                    line = '-'*60
                if line.startswith("'''") or line.endswith("'''"):
                    #end = True
                    param_started = False
                    started = False
                    if line.strip() != "'''":
                        line = line.replace("'''", "")
                        doc_str.append(line)

                    print "L ", line
                    final_doc = "\n".join(doc_str)
                    if count > 300:
                        break
                    else:
                        my.write_to(final_doc, short_title, plain_function)
                        # reset plain_function
                        plain_function = False
                        strip = True
                        doc_str = []
                        continue

                doc_str.append(line)
                if param_started and strip:
                    doc_str.append('')

        my.final_paths = sorted(my.final_paths)
        my.final_func_paths = sorted(my.final_func_paths)

        # put __init__ back to the top
        last = my.final_func_paths.pop()
        my.final_func_paths.insert(0, last)
        my.add_adoc(my.final_paths, my.final_func_paths)
        
    def write_to(my, final_doc, short_title, plain_function=False):
        first = short_title[0]
        if first == '\\':
            first = short_title[2]
            short_title = short_title[2:]
        final_dir = '../section/api/python-client-api/general/%s/python-client-api_general_%s'%(first.capitalize(), short_title)
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)
        final_path = '%s/index.txt'%final_dir
        f = open(final_path, 'w') 
        f.write(final_doc)
        print "write to ", final_path
        if plain_function:
            my.final_func_paths.append('include::%s[]'%final_path)
        else:
            my.final_paths.append('include::%s[]'%final_path)

    def add_adoc(my, final_paths, final_func_paths):
        ''' replace it with new final index.txt lines'''
        adoc_path = '../book/tactic-developer.adoc'
        adoc_path_orig = '../book/tactic-developer.adoc_orig'
        import shutil
        shutil.move(adoc_path, adoc_path_orig)
        new_adoc_path = '../book/tactic-developer.adoc'
        f = open(adoc_path_orig, 'r')
        lines = f.readlines()
        f2 = open(new_adoc_path, 'w')
        start_count = -1
        for line in lines:
            if line.find('TACTIC Python Client API Reference') != -1:
                start_count = 5
            else:
                if start_count > 0:
                    start_count -= 1
            
            if start_count == 0:
                f2.write('\n\n'.join(final_func_paths))
                f2.write('\n\n')
                f2.write('\n\n'.join(final_paths))
                break
            f2.write(line)

        f2.close()
        f.close()


        


if __name__ == '__main__':
    cmd = GenerateApiDoc()
    cmd.execute()

