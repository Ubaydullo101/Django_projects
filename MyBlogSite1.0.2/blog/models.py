from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    photo=models.ImageField(upload_to='images/',   null=True, blank=True)
    views_count=models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_date"]

    def get_absolute_url(self):  # new
        return reverse('article_detail', args=[str(self.id)])

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.title

    @property
    def add_views(self):
        self.views_count +=1
        self.save()
