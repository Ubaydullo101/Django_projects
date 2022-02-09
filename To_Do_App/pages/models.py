from django.db import models
from django.urls import reverse


class To_Do_Task(models.Model):
    task=models.TextField()
    created_data=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):  # new
        return reverse('task_detail', args=[str(self.id)])