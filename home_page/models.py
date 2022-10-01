from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.

class Title(models.Model):
    category_title = models.CharField(_("Category Title"),max_length=250,blank=True,null=True)

    def __str__(self):
        return self.category_title

class TotalSales(models.Model):

    sales = models.IntegerField(_("Sales"),default=0,blank=True,null=True)

    def __str_(self):
        return str(self.sales)
    
    class Meta:
        verbose_name_plural = "Total Sales"


    

class Banner(models.Model):
    heading = models.CharField(max_length=250,blank=True,null=True)
    discription = RichTextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True,upload_to='Banner')

    def __str__(self):
        return self.heading


class Category(models.Model):
    cat_title =models.ForeignKey(Title, on_delete=models.CASCADE)
    total_sales = models.ForeignKey(TotalSales, on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)
    heading = models.CharField(_("Product Heading"),max_length=250,blank=True,null=True)
    discription = RichTextField(_("Discription"),blank=True,null=True)
    price = models.IntegerField(_("Price"),default=0,blank=True,null=True)
    product_url = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.heading

class SectionImage(models.Model):
    section_image = models.ImageField(_("Section3 Image"),blank=True,null=True,upload_to="SectionImage") 
    class Meta:
        verbose_name_plural = "Section Image"
    
    def __str__(self):
        return self.section_image


class Section3(models.Model):
    section_image = models.ForeignKey(SectionImage, on_delete=models.CASCADE)
    section_heading = models.CharField(_("Section3 Heading"),max_length=150,blank=True,null=True)
    section_sub_heading = models.CharField(_("Section3 Sub Heading"),max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.section_heading   

    class Meta:
        verbose_name_plural = "Section 3"

   

    




