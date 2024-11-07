from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Link(models.Model):
    url = models.URLField()
    img = models.ImageField(upload_to='img', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


class Generator(models.Model):
    name = models.CharField(max_length=100)
    content = RichTextUploadingField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id', 'created_at']

    def __str__(self):
        return self.name


