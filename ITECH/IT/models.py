from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.conf import settings
from userprofile.models import UserProfile
from django.urls import reverse
class Restaurant(models.Model):
    Name = models.CharField(max_length=100)  # 文章标题，models.CharField为字符串字段，用于保存较短的字符串
    Introduction = models.TextField( blank=True, null=True)  # 文章正文，TextField用于保存大量文本
    address= models.CharField(max_length=100)
    business_Hours =models.CharField(max_length=100)
    rating = models.IntegerField(default=0, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)  # 文章创建时间，default=timezone.now指定在创建数据时默认写入当前的时间
    updated = models.DateTimeField(auto_now=True)  # 文章更新时间，auto_now=True指定每次数据更新时自动写入当前时间
    main_image = models.ImageField(upload_to="main_images/", verbose_name="main_picture")
    restaurant_image = models.ImageField(upload_to="restaurant_images/", verbose_name="restaurant_picture")
    owner =  models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="restaurants")
    class Meta:  # 内部类，用于定义元数据
        ordering = ('-created',)  # ordering指定模型返回的数据的排列顺序，'-created' 表明数据应该以文章创建时间倒序排列，负号标识倒序

    def __str__(self):  # 定义当调用对象的 str() 方法时的返回值内容
        return self.Name

    def get_absolute_url(self):
        return reverse('IT:restaurant_detail', args=[self.id])

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(verbose_name="comment")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.restaurant.name} ({self.rating} ⭐)"
