from django.contrib import admin
from footer_application.models import *

class  AboutAdmin(admin.ModelAdmin):
    Model= About
    list_display=['heading','discription']
admin.site.register(About,AboutAdmin)

class FooterHeadingAdmin(admin.ModelAdmin):
    Model=FooterHeading
    list_display=['heading_title']
admin.site.register(FooterHeading,FooterHeadingAdmin)

class  ColumnAdmin(admin.ModelAdmin):
    Model= Column
    list_display=['heading','items']
admin.site.register( Column,ColumnAdmin)

