#!/usr/bin/env python3

import argparse
import os
import subprocess


def parse_repo_list(exclude_list):
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
            if repo_name in exclude_list:
                print('Ignoring %s'%repo_name)
                continue

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
            print(f"Command executed: {' '.join(result.args)}")
            print("Stdout:", result.stdout)
            print("Stderr:", result.stderr)
            print("Return code:", result.returncode)
            print('')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Little helper for add SSYP project as submodule (for quick backup)')
    parser.add_argument('--exclude', help='project to exclude', action='append')
    args = parser.parse_args()

    repo_list = parse_repo_list(args.exclude)
    add_submodule_if_need(repo_list)
    print('done.')