import os
import pathlib
from typing import NamedTuple

PREFIX = os.getenv("PREFIX")
TOKEN = os.getenv("TOKEN")

BOT_REPO_URL = "https://github.com/dawnofmidnight/monkebot"

EXTENSIONS = pathlib.Path("bot/exts/")
LOG_FILE = pathlib.Path("log/monke.log")


class Channels(NamedTuple):
    general = 825733815456104451
