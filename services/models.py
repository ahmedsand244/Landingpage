from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon_svg = models.TextField(blank=True, help_text="Raw SVG code for the technology logo")
    description = models.TextField(blank=True)
    category = models.ForeignKey('projects.Category', on_delete=models.CASCADE, related_name='technologies')

    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['name']

    def __str__(self):
        return self.name
