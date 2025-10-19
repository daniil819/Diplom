from django.contrib import admin
from .models import Menu, Personal
from django.utils.safestring import mark_safe


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'recipe', 'ingredients', 'slug', 'price', 'get_img')
    list_editable = ('price', 'slug')

    def get_img(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='80'>")

    get_img.short_description = 'Dish'


class PersonalAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'get_img')

    def get_img(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='80'>")

    get_img.short_description = 'Photography'


admin.site.register(Menu, MenuAdmin)
admin.site.register(Personal, PersonalAdmin)
