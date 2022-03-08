from django.contrib import admin

from bookmarks.models import Bookmark

# Register your models here.


@admin.register(Bookmark)
class BookMarkAdmin(admin.ModelAdmin):
    list_display = ["user", "url"]
