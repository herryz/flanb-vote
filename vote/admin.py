from django.contrib import admin

from vote import models

admin.site.register(models.Vote)
admin.site.register(models.VoteOption)
