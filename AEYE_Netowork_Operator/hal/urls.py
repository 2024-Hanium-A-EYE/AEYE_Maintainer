from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from .views.AEYE_print_log import aeye_hal_print_log_Viewsets

router = DefaultRouter()

router.register(r'print-log', aeye_hal_print_log_Viewsets)



urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

