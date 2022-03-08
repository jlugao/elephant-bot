from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from tgbot.models import User
from bookmarks.models import Bookmark


def return_bookmarks(update: Update, context: CallbackContext) -> None:
    """Show help info about all secret admins commands"""
    user = User.get_user(update, context)
    tags = context.args
    bookmarks = Bookmark.objects.filter(user=user)
    reply = "Bookmarks:\n"
    for bookmark in bookmarks:
        tags = "["
        tags += ", ".join([str(tag) for tag in bookmark.tags.all()])
        tags += "]"
        reply += f" - <a href='{bookmark.url}'>{bookmark.url}</a>\n"
    update.message.reply_text(
        reply,
        parse_mode=ParseMode.HTML,
    )
