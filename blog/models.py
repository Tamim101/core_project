from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100,blank=True,null=False)
    description = models.TextField(max_length=1000,blank=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-updated_at','-created_at']


    def __str__(self):
        return self.description[0:50]
