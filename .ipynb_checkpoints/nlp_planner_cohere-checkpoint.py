#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cohere
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

#  Use the V2 client from the new SDK
co = cohere.ClientV2(api_key=api_key)

def get_intent_plan(user_text):
    messages = [
        {"role": "system", "content": """
        Convert the following natural language instruction into structured JSON for automation.

        Examples:
        User: "Send an email to John saying I’ll be late"
        JSON: {"intent": "send_email", "recipient": "John", "body": "I’ll be late"}

        User: "Summarize the PDF in Downloads"
        JSON: {"intent": "summarize_file", "file_path": "Downloads/latest"}

        User: "Open Spotify and play my chill playlist"
        JSON: {"intent": "open_app", "app_name": "Spotify", "action": "play_playlist", "playlist_name": "chill"}

        Now process this:
        """},
        {"role": "user", "content": f"User: \"{user_text}\"\nJSON:"}
    ]

    response = co.chat(
        model="command-r-plus",
        messages=messages,
        temperature=0.3,
        max_tokens=100,
    )

        #  Extract only the text portion from the assistant's message
    try:
        content_items = response.message.content  # This is a list
        text_blocks = [item.text for item in content_items if hasattr(item, "text")]
        raw_text = "".join(text_blocks).strip()

        #  Remove markdown-style code block formatting
        if raw_text.startswith("```"):
            raw_text = raw_text.strip("`").strip()
            if raw_text.startswith("json"):
                raw_text = raw_text[len("json"):].strip()

        return json.loads(raw_text)

    except Exception as e:
        raw_output = response.message.content if hasattr(response, "message") else "N/A"
        print(f" Parsing failed. Raw output: {raw_output}. Error: {e}")
        return {"intent": "unknown", "raw": user_text}
