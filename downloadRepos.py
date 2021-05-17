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
    def __init__(self, reposYml, wpath):
        with open(reposYml, 'r') as file:
            self.repos = yaml.load(file, Loader=yaml.FullLoader)

        self.wpath = wpath
        try:
            os.mkdir(path)
        except:
            pass

        self.log = {}


    def report(self):
        for r, s in self.log.items():
            print("{}: {}".format(r.split(sep='/')[-1], s))


    def run(self):
        repoFail = []
        for repo in self.repos:
            status = True
            url = 'git@github.com:' + repo
            command = 'clone {} {}/{} '.format(url, self.wpath, repo.split(sep='/')[-1])
            try:
                out = subprocess.check_output('git {}'.format(command), shell=True).decode('utf-8')
            except:
                status = False

            self.log[repo] = status


if __name__ == '__main__':
    argparse.ArgumentParser()
    parser = argparse.ArgumentParser(prog='Download repos url created from github classroom')
    parser.add_argument('--repos', default=None, type=str, help='repos yml')
    parser.add_argument('--save', default=None, type=str, help='Save path')

    args = parser.parse_args()
    dr = downloadRepos(args.repos, args.save)
    dr.run()
    dr.report()
