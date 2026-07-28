from django.db import models

class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General Inquiries'),
        ('technical', 'Technical Details'),
        ('pricing', 'Pricing & Deliverables'),
        ('support', 'Support & Deployment'),
    ]

    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='general', db_index=True)
    order = models.IntegerField(default=0, db_index=True, help_text="Used to control order of items in list")

    class Meta:
        ordering = ['category', 'order', 'question']

    def __str__(self):
        return f"[{self.get_category_display()}] {self.question}"


class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True, help_text="Optional email for notification")
    role_university = models.CharField(max_length=200, help_text="Role or University/Company name")
    review_text = models.TextField()
    rating = models.IntegerField(default=5, choices=[(i, f"{i} Stars") for i in range(1, 6)])
    is_approved = models.BooleanField(default=True, help_text="Approved to show publicly")
    admin_reply = models.TextField(blank=True, null=True, help_text="Official admin reply to this comment")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-created_at', '-id']

    def __str__(self):
        return f"{self.name} ({self.rating}★) - {self.role_university}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150, verbose_name="الاسم الكريم")
    email = models.CharField(max_length=200, verbose_name="البريد أو رقم الهاتف")
    subject = models.CharField(max_length=250, verbose_name="موضوع الاستفسار")
    message = models.TextField(verbose_name="تفاصيل الرسالة")
    is_read = models.BooleanField(default=False, verbose_name="تمت القراءة والمتابعة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")

    class Meta:
        verbose_name = "رسالة استفسار"
        verbose_name_plural = "رسائل واستفسارات التواصل"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"


class SiteSetting(models.Model):
    academic_site_url = models.URLField(
        blank=True, 
        null=True, 
        help_text="رابط موقع/منصة مشاريع التخرج المخصصة (مثال: https://academic-projects.com)"
    )
    academic_button_text = models.CharField(
        max_length=150, 
        default="الانتقال لمنصة مشاريع التخرج الأكاديمية",
        help_text="نص الزر في مسار مشاريع التخرج"
    )

    class Meta:
        verbose_name = "إعدادات الموقع"
        verbose_name_plural = "إعدادات الموقع العامة"

    def __str__(self):
        return "إعدادات الموقع العامة"


class StudioMetric(models.Model):
    THEME_CHOICES = [
        ('primary', 'بنفسجي / Primary'),
        ('emerald', 'أخضر / Emerald'),
        ('secondary', 'أزرق / Secondary'),
        ('amber', 'ذهبي / Amber'),
    ]

    title = models.CharField(max_length=150, help_text="عنوان الإحصائية (مثال: مشروع بزنس و MVP مكتمل)")
    value = models.CharField(max_length=50, help_text="القيمة الرقمية (مثال: +50 أو 100%)")
    subtitle = models.CharField(max_length=200, blank=True, help_text="وصف مكمل (مثال: منصات سحابية وتطبيقات جوال حية)")
    icon_name = models.CharField(max_length=50, default="rocket_launch", help_text="اسم أيقونة Material Symbols (مثل: rocket_launch, workspace_premium, public, code)")
    color_theme = models.CharField(max_length=20, choices=THEME_CHOICES, default='primary')
    order = models.IntegerField(default=0, help_text="ترتيب العرض")
    is_active = models.BooleanField(default=True, help_text="إظهار في الصفحة الرئيسية")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "إحصائية الاستوديو"
        verbose_name_plural = "إحصائيات وإنجازات الاستوديو"

    def __str__(self):
        return f"{self.value} - {self.title}"

