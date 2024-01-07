from django.contrib import admin
from firstapp.models import Hydjobs,Banglorejobs,Punejobs
# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','role','eligibility','location','email','contactnumber']
admin.site.register(Hydjobs,HydjobsAdmin)

class BanglorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','role','eligibility','location','email','contactnumber']
admin.site.register(Banglorejobs,BanglorejobsAdmin)

class PunejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','role','eligibility','location','email','contactnumber']
admin.site.register(Punejobs,PunejobsAdmin)
