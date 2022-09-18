from os import environ
from requests import post
from time import sleep

from history import get_latest_id, store_latest_id
from updates import get_updates, select_new_updates

WEBBOOK_URL = environ["WEBHOOK_URL"]
AVATAR_URL = environ.get("AVATAR_URL")
MSG_DELAY = int(environ["MSG_DELAY"])
FLOOD_PREVENTION_DELAY_SECONDS = 2


def main() -> None:
    while not sleep(MSG_DELAY):
        scraper_monitor()


def scraper_monitor() -> None:
    updates = get_updates()
    new_updates = select_new_updates(updates, get_latest_id())
    for update in new_updates:
        store_latest_id(update.id)
        send_update(update.user, update.content)


def send_update(user: str, content: str) -> None:
    data = {"content": content, "username": user, "avatar_url": AVATAR_URL}
    post(WEBBOOK_URL, data)
    sleep(FLOOD_PREVENTION_DELAY_SECONDS)  # Dirty anti-flood prevention


if __name__ == "__main__":
    main()
