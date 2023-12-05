from django.contrib import admin
from django.utils.html import format_html

from .models import *


class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px"/>'.format(
                obj.image.url
            )
        )

    list_display = ["name", "image_tag", "created_date"]


admin.site.register(Image, ImageAdmin)


admin.site.register(IndexSliderImage)
admin.site.register(IndexTileImage)
