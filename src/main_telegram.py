from os import environ
from time import sleep

from requests import get

from scraper_monitor import scraper_monitor

TELEGRAM_API_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
BOT_TOKEN = environ["BOT_TOKEN"]
MSG_DELAY = int(environ["MSG_DELAY"])
GROUPS = environ["GROUPS"].split(",")


def main() -> None:
    while not sleep(MSG_DELAY):
        scraper_monitor(send_update)


def send_update(user: str, content: str) -> None:
    for group in GROUPS:
        get(TELEGRAM_API_URL.format(BOT_TOKEN, group, f"{user}: {content}"))


if __name__ == "__main__":
    main()
