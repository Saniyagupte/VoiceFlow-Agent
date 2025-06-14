#!/usr/bin/env python
# coding: utf-8

# In[1]:


# handlers.py

def open_file(task):
    import os
    file_type = task.get("file_type", "pdf")
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    for file in os.listdir(downloads_path):
        if file.endswith(f".{file_type}"):
            os.startfile(os.path.join(downloads_path, file))
            return

def open_app(task):
    import os
    app_name = task.get("app_name", "").lower()
    if app_name == "spotify":
        os.system("start spotify")
    elif app_name == "notepad":
        os.system("notepad")

def unknown_intent(task):
    print(f" Unknown intent: {task.get('intent')}")


# In[ ]:




