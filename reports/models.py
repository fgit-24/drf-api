from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Report(models.Model):
    """
    Model for users to report inappropriate posts.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('resolved', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reason = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    class Meta:
        ordering = ['-reported_at']

    def __str__(self):
        return (
            f'Report {self.id} - Post {self.post.id} by {self.user.username}, Status: {self.get_status_display()}'
        )