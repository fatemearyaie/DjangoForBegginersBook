from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("postdetail", kwargs={"pk": self.pk})