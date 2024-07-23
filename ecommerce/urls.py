from django.contrib import admin
from django.urls import path,include
from product_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category',views.CategoryView)
router.register('product',views.ProductView)
router.register('brand',views.BrandView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
