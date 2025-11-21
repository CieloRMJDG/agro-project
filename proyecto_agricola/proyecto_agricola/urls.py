
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from lecturas.views import dashboard_view

# --- Configuración de la documentación Swagger ---
schema_view = get_schema_view(
    openapi.Info(
        title="API Agrícola (Lecturas de Sensores)",
        default_version='v1',
        description="Endpoints para gestionar y consultar lecturas de sensores y unidades de medida.",
        terms_of_service="[https://www.google.com/policies/terms/](https://www.google.com/policies/terms/)",
        contact=openapi.Contact(email="contacto@ejemplo.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# --- Vista de Inicio (Home View) para la raíz ---
def home_view(request):
    return HttpResponse(
        "<h1>¡Servidor de la API Agrícola funcionando!</h1>"
        "<p>La API está disponible en <a href='/api/'>/api/</a>.</p>"
        "<p>La documentación interactiva Swagger está en <a href='/swagger/'>/swagger/</a>.</p>"
    )


urlpatterns = [
    # Ruta de administración
    path('admin/', admin.site.urls),
    
    # Ruta principal de la API (incluye las URLs de la app 'lecturas')
    # Si en tu error viste 'api/v1', cámbialo a path('api/v1/', include('lecturas.urls'))
    path('api/', include('lecturas.urls')),
    
    # Rutas de Documentación (Swagger y Redoc)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # La ruta vacía (RAÍZ). Esta es la que resuelve el 404 en la página principal.
    path('', home_view),
    # Dashboard accesible desde la raíz: /dashboard/
    path('dashboard/', dashboard_view),
]