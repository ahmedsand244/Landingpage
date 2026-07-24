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
    role_university = models.CharField(max_length=200, help_text="Role or University/Company name")
    review_text = models.TextField()
    video_url = models.URLField(blank=True, null=True, help_text="YouTube/Vimeo demo url from testimonial")
    rating = models.IntegerField(default=5, choices=[(i, str(i)) for i in range(1, 6)])
    avatar = models.ImageField(upload_to='testimonials/avatars/', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.role_university}"
