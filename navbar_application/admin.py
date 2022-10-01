from django.contrib import admin
from navbar_application.models import Topsection,Topsection1,Topsection2

# Register your models here.
class TopsectionAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Topsection,TopsectionAdmin)

class Topsection1Admin(admin.ModelAdmin):
    list_display = ['topsection','sub_title']

admin.site.register(Topsection1,Topsection1Admin)

class Topsection2Admin(admin.ModelAdmin):
    list_display = ['topsection1','get_all','items']

    def get_all(self,instance):
        return instance.topsection1.topsection
admin.site.register(Topsection2,Topsection2Admin)

