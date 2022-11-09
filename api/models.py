from django.db import models


class Upload(models.Model):
    file=models.FileField(Upload_to="files")
    created_date=models.DateTimeField(auto_now_add=True)
# Create your models here.
