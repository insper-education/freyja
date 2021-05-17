#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Rafael Corsi @ insper.edu.br
# 2021

import argparse
import yaml
import json
import os
import git
import tempfile
import subprocess
import time

class createIssues():
    def __init__(self, reposYml, issuesYml):
        with open(issuesYml, 'r') as file:
            self.issues = yaml.load(file, Loader=yaml.FullLoader)['issues']

        with open(reposYml, 'r') as file:
            self.repos = yaml.load(file, Loader=yaml.FullLoader)

        self.log = {}


    def run(self):
        self.ghIssueCreateBulk()


    def report(self):
        for r, s in self.log.items():
            print(r)
            for n in s:
                print("{}: {}".format(n[0], n[1]))
        pass


    def ghIssueList(self, repo):
        command = 'issue list -s all -R {}'.format(repo)
        out = subprocess.check_output('gh {}'.format(command), shell=True).decode('utf-8')
        return(out)


    def ghIssueExist(self, issueList, issue):
        if issueList.find(issue['Title']) > 0:
            return True
        return False


    def ghIssueCreeate(self, issue, repo):
        title = '\'{}\''.format(issue['Title'])
        body = '\'{}\''.format(issue['Body'])
        command = 'issue create -t {} -b {} -R {}'.format(title, body, repo)
        process = subprocess.Popen(['gh', command],
                  stdout=subprocess.PIPE,
                  stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stderr


    def ghIssueCreateBulk(self):
        for repo in self.repos:
            log = []
            status = None
            issueList = self.ghIssueList(repo)
            for k, v in self.issues.items():
                if self.ghIssueExist(issueList, v) is False:
 #                   print('criando issue: {}'.format(v['Title']))
                    r = self.ghIssueCreeate(v, repo)
                    if r:
                        status = 'Erro'
                    else:
                        status = 'Created'
                    time.sleep(0)
                else:
                    status = 'Existed'
  #                  print('issue já existia: {}'.format(v['Title']))
                log.append([v['Title'], status])
            self.log[repo] = log


if __name__ == '__main__':
    argparse.ArgumentParser()
    parser = argparse.ArgumentParser(prog='Automatic issue create on github - CLI')
    parser.add_argument('--repos', default=None,  type=str, help='Repositorios (yml)')
    parser.add_argument('--issues', default=None,  type=str, help='Issues (yml)')
    args = parser.parse_args()

    ci = createIssues(args.repos, args.issues)
    ci.run()
    ci.report()
