from django.db import models
from utils.models import CreateUpdateTracker, nb, GetOrNoneManager
from taggit.managers import TaggableManager

# Create your models here.


class Bookmark(CreateUpdateTracker):
    user = models.ForeignKey("tgbot.User", on_delete=models.CASCADE)
    url = models.URLField(**nb)

    tags = TaggableManager()
