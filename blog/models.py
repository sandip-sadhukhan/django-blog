from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     name = models.CharField(max_length=60)
#     commentText = models.CharField(max_length=200)
#     date_created = models.DateTimeField(auto_now_add=True)