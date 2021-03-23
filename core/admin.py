from django.contrib import admin

import core.models as models


@admin.register(models.Auction)
class AuctionAdmin(admin.ModelAdmin):
    pass
