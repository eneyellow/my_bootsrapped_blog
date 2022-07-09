from django.db import models
from django.urls import reverse



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])