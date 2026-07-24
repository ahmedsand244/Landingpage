from django.contrib import admin
from .models import FAQ, Testimonial

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order')
    list_filter = ('category',)
    search_fields = ('question', 'answer')
    ordering = ('category', 'order')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role_university', 'rating')
    list_filter = ('rating',)
    search_fields = ('name', 'role_university', 'review_text')
