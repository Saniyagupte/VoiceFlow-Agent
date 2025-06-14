# 🧠 VoiceFlow Agent – Voice Controlled AI Assistant

VoiceFlow Agent is a voice-operated, modular AI assistant that listens to your spoken commands, understands your intent using an LLM, and executes tasks on your system using specialized handlers. It's built with scalability and clarity in mind — designed to function like a real personal AI assistant.

---

##  Features Implemented

###  1. Voice Input (Speech to Text)
- Captures voice input using the microphone.
- Converts speech to text using OpenAI’s Whisper model.
- Automatically stores audio files with timestamps.

> Example:  
> You say: "Open Spotify" → Whisper transcribes: `"open spotify"`

---

###  2. Intent Detection (Natural Language to JSON Plan)
- Uses Cohere’s Command R+ model to analyze your transcribed command.
- Returns a structured JSON plan with an `intent` and any relevant parameters.

> Example:  
> Input: `"Send an email to Alice"`  
> Output:  
> ```json
> {
>   "intent": "send_email",
>   "recipient": "Alice",
>   "subject": "Hello",
>   "body": "Let's connect at 5"
> }
> ```

---

###  3. Intent Routing via Command Registry
- Every recognized intent is routed to a dedicated handler class.
- Uses a central `COMMAND_REGISTRY` to map intents to handler classes.
- Easily extendable — add new commands by just writing a new handler and registering it.

---

## 🛠️ Handlers Implemented

###  `open_file`
- Opens the most recent file (e.g., `.pdf`, `.txt`) from your Downloads folder.
- Detects file type based on plan parameters.
- Uses platform-specific commands to open files.

---

###  `open_app`
- Opens apps like Spotify, Chrome, Notepad, VSCode, Calculator, etc.
- Cross-platform support (Windows, macOS, Linux).
- Extensible: you can map more apps to commands easily.

---

###  `send_email`
- Sends emails using configured SMTP settings.
- Extracts recipient, subject, and body from the generated plan.
- Ready for Gmail or other providers with app passwords.

---

##  Architecture

```text
+--------------------------+
|  Speech to Text        | ← whisper (speech_to_text.py)
+------------+-------------+
             |
+------------v-------------+
|  LLM Intent Planner    | ← Cohere (nlp_planner_cohere.py)
+------------+-------------+
             |
+------------v-------------+
|  Command Router        | ← command_router.py
+------------+-------------+
             |
+------------v-------------+
| 🛠 Task Handlers         | ← handlers/*.py
+--------------------------+

```
---

##  Future Scope

1.  Calendar & Email Integration**  
   Enable the assistant to schedule meetings, send emails, and check your availability using APIs like Google Calendar and Gmail.

2.  Plugin System for New Intents**  
   Design a plugin-based architecture allowing developers to easily add new capabilities such as booking rides, ordering food, or starting timers.

3.  IoT & Smart Home Control**  
   Control smart devices like lights, fans, or thermostats using protocols such as MQTT or integration with platforms like Home Assistant.

4.  Memory & Context Awareness**  
   Introduce short-term memory to support follow-up questions and long-term memory for storing user preferences and behaviors.
