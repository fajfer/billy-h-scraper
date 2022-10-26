from os import environ
from typing import Any, NamedTuple

from bs4 import BeautifulSoup
from loguru import logger
from requests import get

WEB_URL = environ["WEB_URL"]


class Update(NamedTuple):
    id: int
    user: str
    content: str


def get_updates() -> list[Update]:
    resp = get(WEB_URL)
    soup = BeautifulSoup(resp.text, "html.parser")
    raw_updates = soup.find_all("div", {"class": "listaditem"})[::-1]
    updates = map(parse_update, raw_updates)
    return list(sorted(updates, key=lambda update: update.id))


def parse_update(raw_update: Any) -> Update:
    id = raw_update.find("span", {"class": "aditemfooter"}).find("a").next
    user = raw_update.find("i", {"class": "icon-user"}).next.strip()
    content = raw_update.find("div", {"class": "adcontent"}).next.strip()
    logger.info(f"[{id}] {user}: {content}")
    return Update(int(id), user, content)


def select_new_updates(updates: list[Update], latest_id: int) -> list[Update]:
    return [update for update in updates if update.id > latest_id]
