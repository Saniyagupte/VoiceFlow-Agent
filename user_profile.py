#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

def load_user_profile(path="user_profile.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "name": "User",
            "email": "user@example.com",
            "favorite_music": "chill"
        }

