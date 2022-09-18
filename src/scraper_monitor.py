from typing import Callable
from time import sleep

from history import get_latest_id, store_latest_id
from updates import get_updates, select_new_updates

FLOOD_PREVENTION_DELAY_SECONDS = 2


def scraper_monitor(update_sender: Callable) -> None:
    updates = get_updates()
    new_updates = select_new_updates(updates, get_latest_id())
    for update in new_updates:
        store_latest_id(update.id)
        send_update(update_sender, update.user, update.content)


def send_update(update_sender: Callable, user: str, content: str) -> None:
    update_sender(user, content)
    sleep(FLOOD_PREVENTION_DELAY_SECONDS)  # Dirty anti-flood prevention
