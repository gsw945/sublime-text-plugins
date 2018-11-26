# -*- coding: utf-8 -*-
import os
import sublime
import sublime_plugin


class CopyUnixPathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_path = self.view.file_name()
        unix_path = file_path.replace('\\', '/')
        sublime.set_clipboard(unix_path)
        '''
        window = sublime.active_window()
        self.view.insert(edit, 0, "Hello, World!")
        panel = window.create_output_panel('copy_panel')
        panel.run_command("append", {"characters": "Hello World" + '\t' + unix_path})
        window.run_command('show_panel', {'panel':'output.copy_panel'})
        print(self.view.window().active_panel())
        '''
        
    def is_visible(self):
        return True
    
    def is_enabled(self):
        return bool(self.view.file_name())