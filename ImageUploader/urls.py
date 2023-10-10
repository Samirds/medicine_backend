from django.urls import path
from . views import UploadImage, ShowUploadedImage

urlpatterns = [path("uploadimage/", UploadImage.as_view()),
               path("showuploadedimage/", ShowUploadedImage.as_view()),
               ]