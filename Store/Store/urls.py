
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('product/', include('product.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
