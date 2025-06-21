#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import os

MEMORY_FILE = "memory_store.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

def get_context(key, default=None):
    memory = load_memory()
    return memory.get(key, default)

def set_context(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)

