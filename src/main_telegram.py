from os import environ

from telegram.ext import CallbackContext, Updater

from scraper_monitor import scraper_monitor

BOT_TOKEN = environ["BOT_TOKEN"]
MSG_DELAY = int(environ["MSG_DELAY"])
GROUPS = environ["GROUPS"].split(",")


def main() -> None:
    updater = Updater(token=BOT_TOKEN, use_context=True)
    updater.job_queue.run_repeating(monitor_job, MSG_DELAY)
    updater.start_polling()
    updater.idle()


def monitor_job(context: CallbackContext) -> None:
    scraper_monitor(lambda user, content: send_update(context, user, content))


def send_update(context: CallbackContext, user: str, content: str) -> None:
    for group in GROUPS:
        context.bot.send_message(group, f"{user}: {content}")


if __name__ == "__main__":
    main()
