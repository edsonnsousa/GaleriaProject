from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# Create your models here.
class Post_Fotos(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

