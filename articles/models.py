from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Genre(models.Model):
    class Meta:
        db_table = "genre"
    
    name = models.CharField(max_length=70, default='')

class Animation(models.Model):
    class Meta:
        db_table = "animation"
    
    title = models.CharField(max_length=70, default='')
    original_title = models.CharField(max_length=70, default='')
    genre = models.ManyToManyField(Genre, related_name="animations")
    company = models.CharField(max_length=70, default='')
    rated = models.CharField(max_length=70, default='')
    broadcasted_date = models.CharField(max_length=70, default='')
    chapters = models.CharField(max_length=70, default='')
    story = models.TextField(max_length=256, default='')
    img = models.TextField(max_length=256, default='')