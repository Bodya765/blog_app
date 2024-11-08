from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    text = models.TextField(validators=[MinLengthValidator(10)])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
