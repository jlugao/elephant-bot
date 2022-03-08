from datetime import timedelta

from django.utils.timezone import now
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from . import static_text
from tgbot.models import User
from bookmarks.models import Bookmark
import re

URL_REGEX = r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
TAGS_REGEX = r"\[(.*)\]"


def raw_message(update: Update, context: CallbackContext) -> None:
    """Show help info about all secret admins commands"""
    user = User.get_user(update, context)
    if url := re.search(URL_REGEX, update.message.text, re.IGNORECASE):
        url = url.group(0)
        tags = re.findall(TAGS_REGEX, update.message.text)
        if tags:
            tags = tags[0].split(",")
        bookmark, created = Bookmark.objects.get_or_create(url=url, user=user)
        existing_tags = bookmark.tags.all()
        new_tags = set(tags) - set(existing_tags)
        bookmark.tags.add(*list(new_tags))
        if not created:
            update.message.reply_text("Bookmark already existed")
        else:
            update.message.reply_text("bookmark created")
        tags = "["
        tags += ", ".join([str(tag) for tag in bookmark.tags.all()])
        tags += "]"
        update.message.reply_text(f"Bookmark: {bookmark.url} \n Tags: {tags}")

    else:
        update.message.reply_text(static_text.raw_message_reply)
        update.message.reply_text(update.message.text)
