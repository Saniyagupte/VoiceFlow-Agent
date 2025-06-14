#!/usr/bin/env python
# coding: utf-8

# In[1]:


# agent_executor.py
from command_router import COMMAND_REGISTRY

class TaskExecutor:
    def __init__(self, context=None):
        self.context = context

    def execute(self, task):
        intent = task.get("intent")
        handler_class = COMMAND_REGISTRY.get(intent)
        if handler_class:
            handler = handler_class(task)
            return handler.run()
        else:
            print(f" Unknown intent: {intent}")

# Add this to enable direct import of `execute`
def execute(plan, context=None):
    executor = TaskExecutor(context=context)
    return executor.execute(plan)




