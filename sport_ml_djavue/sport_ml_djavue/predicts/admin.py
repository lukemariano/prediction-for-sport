from django.contrib import admin

from .models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'age', 'height', 'sex', 'predictions', 'date')


admin.site.register(Data, DataAdmin)
