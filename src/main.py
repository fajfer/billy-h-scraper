from os import environ
from time import sleep

from requests import get, post

from history import get_latest_id, store_latest_id
from updates import get_updates, select_new_updates

MSG_DELAY = int(environ["MSG_DELAY"])
FLOOD_PREVENTION_DELAY_SECONDS = 2

TELEGRAM_API_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
BOT_TOKEN = environ.get("BOT_TOKEN")
GROUPS = environ.get("GROUPS")

WEBBOOK_URL = environ.get("WEBHOOK_URL")
AVATAR_URL = environ.get("AVATAR_URL")


def main() -> None:
    while not sleep(MSG_DELAY):
        updates = get_updates()
        new_updates = select_new_updates(updates, get_latest_id())
        for update in new_updates:
            store_latest_id(update.id)
            send_update(update.user, update.content)


def send_update(user: str, content: str) -> None:
    if BOT_TOKEN and GROUPS:
        send_update_telegram(user, content)
    if WEBBOOK_URL:
        send_update_discord(user, content)


def send_update_telegram(user: str, content: str) -> None:
    for group in GROUPS.split(","):
        get(TELEGRAM_API_URL.format(BOT_TOKEN, group, f"{user}: {content}"))


def send_update_discord(user: str, content: str) -> None:
    data = {"content": content, "username": user, "avatar_url": AVATAR_URL}
    post(WEBBOOK_URL, data)


if __name__ == "__main__":
    main()
