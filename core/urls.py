from django.contrib import admin
from django.urls import path
#se importa para ara configurar la gestión de archivos estáticos y medios 
#en Django durante el desarrollo.
from django.conf.urls.static  import static
#se importa para vincular el arhivo settings
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
