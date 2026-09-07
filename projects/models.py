from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_en = models.CharField(max_length=100, blank=True, help_text="English Category Name")
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    PROJECT_TYPES = [
        ('graduation', 'Academic / Graduation Project'),
        ('commercial', 'Commercial / B2B Solution'),
    ]

    title = models.CharField(max_length=200, unique=True)
    title_en = models.CharField(max_length=200, blank=True, help_text="English Title")
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, default='graduation', db_index=True)
    client_name = models.CharField(max_length=150, help_text="University name or Client name")
    client_name_en = models.CharField(max_length=150, blank=True, help_text="English Client name")
    country = models.CharField(max_length=100, default="Egypt")
    country_en = models.CharField(max_length=100, default="Egypt", blank=True)
    summary = models.TextField(help_text="A brief short summary of the project in Arabic.")
    summary_en = models.TextField(blank=True, help_text="A brief short summary of the project in English.")
    overview = models.TextField(help_text="Detailed overview of architecture and features in Arabic.")
    overview_en = models.TextField(blank=True, help_text="Detailed overview of architecture and features in English.")
    
    # Live Project Link / Demo URL
    project_url = models.URLField(blank=True, null=True, help_text="رابط المعاينة المباشرة أو التجربة الحية للمشروع (Live Demo / Project URL)")
    
    # Many-to-many relationship with Technology
    technologies = models.ManyToManyField('services.Technology', related_name='projects', blank=True)
    
    demo_video_url = models.URLField(blank=True, null=True, help_text="YouTube/Vimeo embed or MP4 video URL")
    
    # Store deliverables as a JSON list
    deliverables = models.JSONField(default=list, blank=True, help_text="List of deliverables in Arabic")
    deliverables_en = models.JSONField(default=list, blank=True, help_text="List of deliverables in English")
    
    is_featured = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def project_type_label_ar(self):
        return "حلول البزنس والشركات" if self.project_type == 'commercial' else "مشروع تخرج أكاديمي"

    @property
    def project_type_label_en(self):
        return "Business Solution" if self.project_type == 'commercial' else "Academic Project"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class ProjectGallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            try:
                from PIL import Image, ImageOps
                from io import BytesIO
                from django.core.files.base import ContentFile
                import os

                img = Image.open(self.image)
                img = ImageOps.exif_transpose(img)

                # Max web resolution: 1600x1200
                max_width, max_height = 1600, 1200
                if img.width > max_width or img.height > max_height:
                    img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

                # Convert to RGB if RGBA/P
                if img.mode in ('RGBA', 'P', 'LA'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'RGBA':
                        background.paste(img, mask=img.split()[3])
                    else:
                        background.paste(img)
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')

                buffer = BytesIO()
                img.save(buffer, format='JPEG', quality=82, optimize=True, progressive=True)
                buffer.seek(0)

                base_name = os.path.splitext(os.path.basename(self.image.name))[0]
                self.image.save(f"{base_name}.jpg", ContentFile(buffer.getvalue()), save=False)
            except Exception:
                pass
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Gallery image for {self.project.title}"

