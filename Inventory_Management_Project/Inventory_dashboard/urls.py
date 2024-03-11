from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('products/', views.products, name='products'),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)