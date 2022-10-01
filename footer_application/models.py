from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    heading=models.CharField(max_length=100,null=True,blank=True)
    discription = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.heading
        
class FooterHeading(models.Model):
    
    heading_title=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.heading_title
    

class Column(models.Model):

    heading=models.ForeignKey(FooterHeading, on_delete=models.CASCADE,null=True,blank=True,)
    items=models.CharField(max_length=100,null=True,blank=True)
   
    def __str__(self):
        return self.items

