from django.contrib.admin import ModelAdmin, register

from nkpro.multi.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('creation', 'titulos', 'slug', 'yt_id')
    ordering = ('creation',)
    prepopulated_fields = {'slug': ('titulos',)}
