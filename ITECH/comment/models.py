from django.db import models
from IT.models import Restaurant
from userprofile.models import UserProfile


class Comment(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    body = models.TextField()
    rating = models.IntegerField(
        choices=[(1, '1 ⭐'), (2, '2 ⭐'), (3, '3 ⭐'), (4, '4 ⭐'), (5, '5 ⭐')],
        default=5
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]
# Create your models here.
