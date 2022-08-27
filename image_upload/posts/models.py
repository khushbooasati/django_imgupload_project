from django.db import models

# Create your models here.
class Posts (models.Model):
    my_name = models.CharField(max_length=50)
    posts_main_img = models.ImageField(upload_to='images/')   
    
     
    def __str__(self):
        return self.my_name   