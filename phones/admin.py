from django.contrib import admin


@admin.register
class PhonesAdmin(admin.ModelAdmin):
    fields = '__all__'
