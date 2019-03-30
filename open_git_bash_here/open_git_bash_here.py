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
        if args[0] is None:
            err_msg = '未能找到 git-bash.exe，请将其所在文件夹添加到环境变量PATH中'
            sublime.message_dialog(err_msg)
        else:
            subprocess.Popen(args, cwd=dir_name, env=env, shell=True)

    def get_git_path(self):
        '''获取Git-Bash绝对路径'''
        git_path = None
        for item in os.environ['PATH'].split(os.pathsep):
            if os.path.exists(os.path.join(item, 'git-bash.exe')):
                git_path = os.path.join(item, 'git-bash.exe')
                break
        if git_path is None:
            git_exe = subprocess.check_output(['where', 'git.exe'])
            git_exe = git_exe.decode('utf-8', 'ignore').strip()
            git_base_dir = os.path.dirname(os.path.dirname(git_exe))
            if os.path.exists(os.path.join(git_base_dir, 'git-bash.exe')):
                git_path = os.path.join(git_base_dir, 'git-bash.exe')
        return git_path
        
    def is_visible(self):
        return True
    
    def is_enabled(self):
        return bool(self.view.file_name())
