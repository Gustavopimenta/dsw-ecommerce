from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuração para servir arquivos de mídia durante o desenvolvimento.
# Mapeia as URLs de mídia especificadas em MEDIA_URL para os arquivos físicos em MEDIA_ROOT.





#criando o login 12:00 (parte 10)