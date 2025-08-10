#!/usr/bin/env python3

import os
import subprocess

def parse_repo_list():
    ret = []
    search_line = 'https://github.com/ssyp-ru/'
    with open('README.md', 'r') as file:
        for line in file:
            index = line.find(search_line)
            if index == -1:
                continue
            
            closed_bracket = line.find(')', index)
            url = line[index:closed_bracket]
            repo_name = line[index+len(search_line):closed_bracket]
            sp = repo_name.split('-', 1)
            year, ws = sp[0], sp[1]

            ret.append((url, year, ws))
    return ret

def add_submodule_if_need(repo_list):
    root_folder = 'submodules'
    for url, year, ws in repo_list:
        folder_path = os.path.join(root_folder, year, ws)
        if not os.path.exists(folder_path):
            print('add git submodule for url=%s path=%s'%(url, folder_path))
            result = subprocess.run(['git', 'submodule', 'add', url, folder_path], capture_output=True, text=True)
            print("Stdout:", result.stdout)
            print("Stderr:", result.stderr)
            print("Return code:", result.returncode)
            print('')

if __name__ == '__main__':
    repo_list = parse_repo_list()
    add_submodule_if_need(repo_list)
    print('done.')