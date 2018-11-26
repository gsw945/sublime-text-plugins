# -*- coding: utf-8 -*-
import os
import subprocess
import sublime
import sublime_plugin


class OpenGitBashHereCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_path = self.view.file_name()
        dir_name = os.path.dirname(os.path.abspath(file_path))
        env = os.environ.copy()
        args = [self.get_git_path()]
        subprocess.Popen(args, cwd=dir_name, env=env, shell=True)

    def get_git_path(self):
        '''获取Git-Bash绝对路径'''
        git_path = None
        for item in os.environ['PATH'].split(os.pathsep):
            if os.path.exists(os.path.join(item, 'git-bash.exe')):
                git_path = os.path.join(item, 'git-bash.exe')
                break
        return git_path
        
    def is_visible(self):
        return True
    
    def is_enabled(self):
        return bool(self.view.file_name())