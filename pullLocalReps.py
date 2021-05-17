#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Rafael Corsi @ insper.edu.br
# 2021

import argparse
import yaml
import os
import subprocess
from joblib import Parallel, delayed

class pullLocalReps():
    def __init__(self, reposPath, force):
        self.reposPath = reposPath
        if not os.path.exists(reposPath):
            print('Path not found')
            return

        self.log = {}


    def report(self):
        for r, s in self.log.items():
            print("{}: {}".format(r.split(sep='/')[-1], s))


    def run(self):
        repoFail = []
        for repo in os.listdir(self.reposPath):
            path = os.path.join(self.reposPath, repo)
            print(path)
            status = True
            command = '-C {} pull origin master'.format(path)
            try:
               out = subprocess.check_output('git {}'.format(command), shell=True).decode('utf-8')
            except:
               status = False

            self.log[repo] = out


if __name__ == '__main__':
    argparse.ArgumentParser()
    parser = argparse.ArgumentParser(prog='Update local repositories from upstream')
    parser.add_argument('--path', default=None, type=str, help='repos path')

    args = parser.parse_args()
    plp = pullLocalReps(args.path, 1)
    plp.run()
    plp.report()
