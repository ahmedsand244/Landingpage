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
