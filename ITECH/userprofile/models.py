from django.db import models
from django.contrib.auth.models import AbstractUser

class UserCategory(models.TextChoices):
    USER = 'user', '普通用户'
    ADMIN = 'admin', '管理员'

class UserProfile(AbstractUser):
    avatar = models.ImageField(upload_to="avatar/", default="avatar/default/default.png",blank=True, null=True)
    category = models.CharField(
        max_length=5,
        choices=UserCategory.choices,
        default=UserCategory.USER,
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username