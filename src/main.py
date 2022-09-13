from os import environ
from time import sleep

from telegram.ext import CallbackContext, Updater

from history import get_latest_id, store_latest_id
from updates import Update, get_updates, select_new_updates

BOT_TOKEN = environ["BOT_TOKEN"]
MSG_DELAY = int(environ["MSG_DELAY"])
GROUPS = environ["GROUPS"].split(",")
FLOOD_PREVENTION_DELAY_SECONDS = 2


def main() -> None:
    updater = Updater(token=BOT_TOKEN, use_context=True)
    updater.job_queue.run_repeating(scraper_monitor, MSG_DELAY)
    updater.start_polling()
    updater.idle()


def scraper_monitor(context: CallbackContext) -> None:
    updates = get_updates()
    new_updates = select_new_updates(updates, get_latest_id())
    for update in new_updates:
        store_latest_id(update.id)
        send_update(context, update)


def send_update(context: CallbackContext, update: Update) -> None:
    for group in GROUPS:
        context.bot.send_message(group, f"{update.user}: {update.content}")
    sleep(FLOOD_PREVENTION_DELAY_SECONDS)  # Dirty anti-flood prevention


if __name__ == "__main__":
    main()
