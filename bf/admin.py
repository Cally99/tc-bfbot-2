from django.contrib import admin
from bf.models import Race, Horse, RaceData, RaceResult, Trainer, Jockey

class RaceInline(admin.TabularInline):
    model = RaceData

class HorseInline(admin.TabularInline):
    model = Horse

class RaceAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']
    inlines = [RaceInline]

class HorseAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']
    inlines = [RaceInline]

class TrainerAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']
    inlines = [HorseInline]

class JockeyAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name', 'weight']

class RaceResultAdmin(admin.ModelAdmin):
    list_filter = ['market_id']

admin.site.register(Race, RaceAdmin)
admin.site.register(Horse, HorseAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Jockey, JockeyAdmin)
admin.site.register(RaceResult, RaceResultAdmin)
