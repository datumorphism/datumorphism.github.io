import configparser
import json
from pathlib import Path
import os
from loguru import logger

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)

from dotenv import load_dotenv

load_dotenv("automation/.env")


class Markdown:
    """
    Class for generating markdown including metadata.
    """
    def __init__(self, content, metadata=None):
        self.markdown = ""
        self.content = content
        self.metadata = metadata

        if self.metadata:
            self.add_metadata()
        self.add_content()

    def add_metadata(self):
        """
        Add metadata to the markdown.
        """
        self.markdown += f"\n\n{self.metadata}"

    def add_content(self):
        """
        Add content to the markdown.
        """
        self.markdown += self.content

    def append_text(self, text):
        """
        Add text to the markdown.
        """
        self.markdown += text




class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)

# Reading Configs

# Setting configuration values
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
api_hash = str(api_hash)

# phone = config['Telegram']['phone']
# username = config['Telegram']['username']
username = os.getenv('TELEGRAM_USERNAME')
chat = "amneumarkt"

# all_messages = []

# with TelegramClient("LMDispatch", api_id, api_hash) as client:
#     for message in client.iter_messages(chat):
#         all_messages.append(message.to_dict())
#         print(message.sender_id, ':', message.text)
#         print(message.to_dict())
#         print(message.to_json())
#         print(message.message)
#         print(message.id)

tg_config = {
    "api_id": api_id,
    "api_hash": api_hash,
    "username": username,
    "chat": chat
}

class Messages:
    """Deal with telegram messages"""
    def __init__(self, target, tg_config):
        if isinstance(target, str):
            target = Path(target)
        self.target = target
        self.tg_config = tg_config

        self.existing_messages = self._existing_messages()


    def _merge_messages(self):
        """merge existing messages and downloaded messages"""
        self.new_messages = []
        existing_ids = [m["id"] for m in self.existing_messages]
        for message in self.downloaded_messages:
            if message["id"] not in existing_ids:
                self.new_messages.append(message)

        self.new_messages = [
            self._add_tags(i) for i in self.new_messages
        ]

        return self.new_messages + self.existing_messages

    def _existing_messages(self):
        """Load messages from json file"""

        if not self.target.is_file():
            logger.warning(f"{self.target} does't exist. Existing message is empty.")
            return []

        with open(self.target, "r") as fp:
            existing_messages = json.load(fp)

        return existing_messages

    def save_messages(self, exclude=None, multifile=True):
        """Save all messages as json file"""

        if exclude is None:
            exclude = ["MessageService"]

        if self.new_messages:
            if multifile is True:
                for i in self.messages:
                    if i.get("_") not in exclude:
                        with open(
                            self.target / f"{i['id']}.json", "w"
                        ) as fp:
                            json.dump(i, fp, cls=DatetimeEncoder, indent=4)
            else:
                with open(self.target, "w") as fp:
                    json.dump(
                        [i for i in  self.messages if i.get("_") not in exclude ], fp, cls=DatetimeEncoder, indent=4
                    )

    def download_messages(self):
        """Return all messages"""

        all_messages = []
        api_hash = self.tg_config["api_hash"]
        api_id = self.tg_config["api_id"]
        username = self.tg_config["username"]
        chat = self.tg_config["chat"]

        with TelegramClient("LMDispatch", api_id, api_hash) as client:
            for message in client.iter_messages(chat):
                all_messages.append(message.to_dict())

        return all_messages

    def _add_tags(self, message):
        """Get tags from message"""
        message_content = message.get("message", "")

        tags = []
        tags_text = message_content.split("\n")[0]
        if not tags_text.startswith("#"):
            tags = []
        else:
            tags = tags_text.split("#")
            tags = [i.strip() for i in tags if i.strip()]

        message["tags"] = tags

        return message

    def run(self):
        """get ready for the messages"""

        self.downloaded_messages = self.download_messages()
        self.messages = self._merge_messages()
        self.save_messages()




# m = Messages(target="data/amneumarkt/all_messages.json", tg_config=tg_config)
m = Messages(target="data/amneumarkt/messages", tg_config=tg_config)

m.run()
