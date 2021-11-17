from django.contrib import admin
from .models import Contact, Newsletter
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    """Create Contact form section in Admin Panel"""
    readonly_fields = (
        'subject',
        'full_name',
        'email',
        'message',
        'date_posted',
    )
    list_display = (
        'full_name',
        'subject',
        'email',
        'date_posted',
    )

    ordering = ('-date_posted',)


admin.site.register(Contact, ContactAdmin)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'subscription_email',
        'date_sent',
        )


admin.site.register(Newsletter, NewsletterAdmin)
