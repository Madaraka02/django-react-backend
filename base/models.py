from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    required_skills = models.TextField()
    company = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)