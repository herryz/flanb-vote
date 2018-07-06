from django.contrib import admin

from polls import models

admin.site.register(models.Vote)
admin.site.register(models.VoteOption)
