from django.contrib import admin
from myapp import models
# Register your models here.
class TopicAdminView(admin.ModelAdmin):
    list_display=('topic_name',)
    search_fields=('topic_name',)
class WebpageAdminView(admin.ModelAdmin):
    list_display=('topic','name','url')
    search_fields=('name',)
    list_filter=('topic','name',)
    list_editable=('name','url')
class AccessDetailAdminView(admin.ModelAdmin):
    list_display=('webpage','datetime')
    search_fields=('datetime',)
admin.site.register(models.Topic,TopicAdminView)
admin.site.register(models.Webpage,WebpageAdminView)
admin.site.register(models.AccessDetail,AccessDetailAdminView)