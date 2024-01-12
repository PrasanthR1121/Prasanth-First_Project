from django.contrib import admin
# from .models import Topic,webPage,accessRecord
from .models import *

admin.site.register(Topic)
admin.site.register(webPage)
admin.site.register(accessRecord)
admin.site.register(user_profileInfo)
