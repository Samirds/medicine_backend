from django.contrib import admin
from .models import PrescriptionImage
# Register your models here.




@admin.register(PrescriptionImage)
class ImageAdmin(admin.ModelAdmin):
    # list_display = ['Username', "UserId","image"]
    list_display = ['Username', "user_email", "uploaded_at", "image"]
    

