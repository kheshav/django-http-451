from django.contrib import admin
from .models import http451_URLS

# Register your models here.


@admin.register(http451_URLS)
class http451_URLS_Admin(admin.ModelAdmin):
    list_display = ('urls_to_block', 'censorship_title', 'block_by_country', "country_code")
    pass
