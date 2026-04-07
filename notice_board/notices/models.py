from django.db import models
from django.utils import timezone
from django.db.models import Q

class Notice(models.Model):
    CATEGORY_CHOICES = [
        ('exam', 'Exam'),
        ('event', 'Event'),
        ('general', 'General'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='general')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    publish_date = models.DateTimeField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def is_active(self):
        now = timezone.now()
        if self.publish_date and self.publish_date > now:
            return False
        if self.expiry_date and self.expiry_date < now:
            return False
        return True
