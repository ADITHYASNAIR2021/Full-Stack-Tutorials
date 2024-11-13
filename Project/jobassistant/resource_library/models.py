from django.db import models

class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('resume', 'Resume Templates'),
        ('cover_letter', 'Cover Letter Templates'),
        ('guide', 'Guides'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='resources/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='guide')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
