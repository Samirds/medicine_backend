
from django.contrib import admin
from django.urls import path, include

# we are doing it  because we are wanting upload pic
from django.conf import settings  
from django.conf.urls.static import static






urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('api.urls')),
    path("user/", include("users.urls")),
    path("imageupload/", include("ImageUploader.urls")),
    path('payment/', include("paymentDetails.urls")),
    #path('googleMap/', include("googleMap.urls")),
    path('orders/', include("orders.urls"))
    
]

 # ------------------------------------  we are doing it  because we are wanting upload pic ---------------------------------
# if Settings.DEBUG:
#     urlpatterns+=static(Settings.MEDIA_URL, document_root = Settings.MEDIA_ROOT)


urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)