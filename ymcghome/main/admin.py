from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import *

# Register your models here.
admin.site.register(RecruitingBanner)
admin.site.register(Introduction)
admin.site.register(Youtube)
admin.site.register(Logo)
admin.site.register(KeyValue)
admin.site.register(Footer)
admin.site.register(Greeting)
admin.site.register(About, MarkdownxModelAdmin)
admin.site.register(Activities, MarkdownxModelAdmin)
admin.site.register(Join, MarkdownxModelAdmin)
# admin.site.register(Elements, MarkdownxModelAdmin)