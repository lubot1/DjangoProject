import os
from django.conf import settings
from django.db import models

def image_dir():
    return os.path.join(settings.BASE_DIR, 'Images')
# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=255)
    file = models.FilePathField(path=image_dir)
    description = models.TextField()
    # lister = models.ForeignKey(Users,on_delete="cascade")
