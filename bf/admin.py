from django.contrib import admin
from bf.models import Race, Horse, RaceData

class RaceInline(admin.TabularInline):
    model = RaceData

class RaceAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']
    inlines = [RaceInline]

class HorseAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']
    inlines = [RaceInline]

admin.site.register(Race, RaceAdmin)
admin.site.register(Horse, HorseAdmin)
