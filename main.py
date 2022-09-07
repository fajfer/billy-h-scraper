from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from requests import get
from bs4 import BeautifulSoup
from loguru import logger
from time import sleep


def scraper_monitor(context: CallbackContext) -> None:
    resp = get(os.environ["WEB_URL"])
    soup = BeautifulSoup(resp.text, "html.parser")
    raw_messages = soup.find_all("div", {"class": "listaditem"})[::-1]
    for message in raw_messages:
        with open("history") as histfile:
            old_msg_id = histfile.read()
            try:
                int(old_msg_id)
            except ValueError:
                old_msg_id = 0
        msg_id = message.find("span", {"class": "aditemfooter"}).find("a").next
        msg_content = message.find("div", {"class": "adcontent"}).next.strip()
        user = message.find("i", {"class": "icon-user"}).next.strip()
        logger.info(f"[{msg_id}] {user}: {msg_content}")

        if int(msg_id) > int(old_msg_id):
            with open("history", "w") as histfile:
                histfile.write(msg_id)
                for group in os.environ["GROUPS"].split(","):
                    context.bot.send_message(group, f"{user}: {msg_content}")
                sleep(2)


updater = Updater(token=os.environ["BOT_TOKEN"], use_context=True)

job_queue = updater.job_queue
job_queue.run_repeating(scraper_monitor, os.environ["MSG_DELAY"])

updater.start_polling()
updater.idle()
