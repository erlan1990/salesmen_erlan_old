from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(House)

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'mark', 'model']  # Отображаем поля в списке объектов

# @admin.register(House)
# class HouseAdmin(admin.ModelAdmin):
#     list_display = ['id', 'photo', 'name']  # Отображаем поля в списке объектов



# @admin.register(Auto)
# class AutoAdmin(admin.ModelAdmin):
#     list_display = ('photo_preview', 'mark', 'model', 'year', 'price')
#     # Другие настройки административного интерфейса

#     def photo_preview(self, obj):
#         return obj.photo.url if obj.photo else 'No Image'
#     photo_preview.short_description = 'Preview'

