from django.db import models

# Create your models here.

class Topsection(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.title

class Topsection1(models.Model):
    topsection = models.ForeignKey(Topsection, on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.sub_title

class Topsection2(models.Model):
    topsection1 = models.ForeignKey(Topsection1, on_delete=models.CASCADE)
    items = models.CharField(max_length=100,blank=True,null=True)
    

    def __str__(self):
        return self.items