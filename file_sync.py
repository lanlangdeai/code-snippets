#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import ntpath
import os
import re
import platform

from subprocess import call
from shutil import copy
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# git root path for files to push to remote
DIR_FOR_GIT = os.path.dirname(os.path.abspath(__file__))

# files to synchronize
SYNC_FILE_LIST = [
    'Cpc-Redis汇总.md',
    'Cpc相关项目(MySQL+Redis).md',
    'Cpc-MySQL汇总.md',
]


class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # print('文件发生变化')
        src_path = event.src_path.replace('\\', '/')
        base_name = os.path.basename(src_path)
        # print('base_name:', base_name)
        if base_name in SYNC_FILE_LIST:
            # print('src_path:', src_path)
            os.chdir(DIR_FOR_GIT)
            git_add_cmd = "git add -A"
            git_commit_cmd = "git commit -m " + re.escape("Update " + base_name)
            if platform.system() == "Windows":
                git_commit_cmd = "git commit -m Update."
            git_pull_cmd = "git pull origin main"
            git_push_cmd = "git push origin main"
            call(
                git_add_cmd + "&&" +
                git_commit_cmd + "&&" +
                git_pull_cmd + "&&" +
                git_push_cmd,
                shell=True
            )


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileChangeHandler()

    for file_path in SYNC_FILE_LIST:
        file_path = os.path.join(DIR_FOR_GIT, file_path)
        # print('当前文件路径', file_path)
        observer.schedule(event_handler, path=os.path.dirname(os.path.realpath(file_path)), recursive=False)

    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        # print('服务中断')
        observer.stop()
    observer.join()
