# handlers/open_file.py

import os

class OpenFileHandler:
    def __init__(self, plan):
        self.plan = plan

    def run(self):
        file_type = self.plan.get("file_type", "pdf")
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        for file in os.listdir(downloads_path):
            if file.endswith(".pdf"):
                file_path = os.path.join(downloads_path, file)
                os.startfile(file_path)  # Windows
                print(f" Opened file: {file_path}")
                return
        print(" No matching file found.")
