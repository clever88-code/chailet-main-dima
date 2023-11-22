from django.contrib import admin
from .models import booking, Hall, News, Menu
# Register your models here.
admin.site.register(booking)
admin.site.register(Hall)
admin.site.register(News)
admin.site.register(Menu)
