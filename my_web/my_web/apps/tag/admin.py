from django.contrib import admin

from my_web.apps.tag.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'is_publish','created_by')
    # raw_id_fields = ('channel_id',)
    # radio_fields = {"channel_id": admin.HORIZONTAL}

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super(TagAdmin, self).save_model(request, obj, form, change)


admin.site.register(Tag, TagAdmin)