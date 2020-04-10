from django.contrib import admin
from topic.models import TopicRecord, Topic2User, Annex
# Register your models here.

admin.site.register(TopicRecord)
admin.site.register(Topic2User)

admin.site.register(Annex)