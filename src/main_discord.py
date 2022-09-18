from os import environ
from time import sleep

from requests import post

from scraper_monitor import scraper_monitor

WEBBOOK_URL = environ["WEBHOOK_URL"]
AVATAR_URL = environ.get("AVATAR_URL")
MSG_DELAY = int(environ["MSG_DELAY"])


def main() -> None:
    while not sleep(MSG_DELAY):
        scraper_monitor(send_update)


def send_update(user: str, content: str) -> None:
    data = {"content": content, "username": user, "avatar_url": AVATAR_URL}
    post(WEBBOOK_URL, data)


if __name__ == "__main__":
    main()
