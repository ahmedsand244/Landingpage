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
    list_display = ('name', 'role_university', 'rating', 'is_approved', 'has_admin_reply', 'created_at')
    list_filter = ('is_approved', 'rating', 'created_at')
    search_fields = ('name', 'role_university', 'review_text', 'admin_reply')
    list_editable = ('is_approved',)

    fieldsets = (
        ('بيانات التعليق والعميل', {
            'fields': ('name', 'email', 'role_university', 'rating', 'review_text', 'is_approved')
        }),
        ('رد إدارة الاستوديو', {
            'fields': ('admin_reply',),
            'description': 'اكتب ردك الرسمي هنا وسيظهر مباشرة أسفل تعليق العميل في الموقع.'
        }),
    )

    def has_admin_reply(self, obj):
        return bool(obj.admin_reply)
    has_admin_reply.boolean = True
    has_admin_reply.short_description = "تم الرد"
