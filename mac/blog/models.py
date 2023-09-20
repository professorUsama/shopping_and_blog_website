from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300, default='')
    heading0 = models.CharField(max_length=150, default='')
    content0 = models.CharField(max_length=10000, default='')
    heading1 = models.CharField(max_length=150, default='')
    content1 = models.CharField(max_length=10000, default='')
    heading2 = models.CharField(max_length=150, default='')
    content2 = models.CharField(max_length=10000, default='')
    publish_date = models.DateField()
    post_thumbnail = models.ImageField(upload_to='blog/imgages', default='')


    def __str__(self):
        return self.title
    