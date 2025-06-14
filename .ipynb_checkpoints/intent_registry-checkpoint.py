#!/usr/bin/env python
# coding: utf-8

# In[1]:


# intent_registry.py
INTENTS = {}

def register_intent(intent_name):
    def wrapper(cls):
        INTENTS[intent_name] = cls
        return cls
    return wrapper

# usage
@register_intent("turn_on_light")
class TurnOnLightHandler:
    def execute(self, task): ...


# In[ ]:




