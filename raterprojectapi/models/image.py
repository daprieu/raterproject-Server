class Image(models.Model):
  
    # file will be uploaded to MEDIA_ROOT / uploads
    upload = models.ImageField(upload_to ='uploads/')