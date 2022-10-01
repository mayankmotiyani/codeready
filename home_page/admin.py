from django.contrib import admin
from home_page.models import Title,TotalSales,Category,SectionImage,Section3,Banner

# Register your models here.
admin.site.register(Title)
admin.site.register(TotalSales)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['get_title','get_sales','heading','discription','price']

    
    def get_title(self,obj):
        return obj.cat_title.category_title

    def get_sales(self,instance):
        return instance.total_sales.sales


class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display = ['heading','discription','image']



    

    
admin.site.register(Banner,BannerAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(SectionImage)
admin.site.register(Section3)





