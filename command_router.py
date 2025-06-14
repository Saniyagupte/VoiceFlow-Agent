# command_router.py
# command_router.py

from handlers.open_file import OpenFileHandler
from handlers.send_email import SendEmailHandler
from handlers.open_app import OpenAppHandler
from handlers.open_app import OpenAppHandler


COMMAND_REGISTRY = {
    "open_file": OpenFileHandler,
    "send_email": SendEmailHandler,
    "open_app": OpenAppHandler,
    "summarize_file": SummarizeFileHandler,
    "check_weather": CheckWeatherHandler,
    "turn_on_device": TurnOnDeviceHandler,
    "schedule_meeting": ScheduleMeetingHandler,
    "read_emails": ReadEmailsHandler,
    "play_music": PlayMusicHandler,
    "browse_web": BrowseWebHandler,
    # Add more as your use cases grow
}
