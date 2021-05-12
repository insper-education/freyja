#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Rafael Corsi @ insper.edu.br
# 2021
#

import argparse
import yaml
import os
import subprocess
from joblib import Parallel, delayed

class downloadRepos():
    def __init__(self, yml, wpath):
        with open(yml, 'r') as file:
            self.repoList = yaml.load(file, Loader=yaml.FullLoader)
        self.wpath = wpath
        try:
            os.mkdir(path)
        except:
            pass
        l = self.download()
        print(l)


    def download(self):
        repoFail = []
        for n in self.repoList:
            url = 'git@github.com:' + n
            command = 'git clone {} {}/{} '.format(url, self.wpath, n)
            try:
                raw = subprocess.check_output(command, shell=True).decode('utf-8')
            except:
                repoFail.append(n)

if __name__ == '__main__':
    argparse.ArgumentParser()
    parser = argparse.ArgumentParser(prog='Download repos url created from github classroom')
    parser.add_argument('--config', default=None, type=str, help='repos yml')
    parser.add_argument('--save', default=None, type=str, help='Save path')

    args = parser.parse_args()
    r = downloadRepos(args.config, args.save)
