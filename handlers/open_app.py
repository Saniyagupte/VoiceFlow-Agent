#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import platform
import subprocess

# handlers/open_app.py

class OpenAppHandler:
    def __init__(self, task):
        self.task = task

    def run(self):
        app_name = self.task.get("app_name", "").lower()

        if app_name not in self.APP_COMMANDS:
            print(f" App '{app_name}' is not supported yet.")
            return

        command = self.APP_COMMANDS[app_name]

        import os, platform, subprocess
        try:
            if platform.system() == "Windows":
                os.system(f"start {command}")
            elif platform.system() == "Darwin":
                subprocess.run(["open", "-a", command])
            elif platform.system() == "Linux":
                subprocess.Popen([command])
            else:
                print(" Unsupported OS")
                return

            print(f" Launching {app_name}...")
        except Exception as e:
            print(f" Failed to open {app_name}: {e}")

    APP_COMMANDS = {
        "spotify": "spotify",
        "notepad": "notepad",
        "vscode": "code",
        "chrome": "chrome",
        "calculator": "calc",
    }




