from django.contrib import admin
from django.urls import path, include
from product_app import views
from rest_framework.routers import DefaultRouter

# this is used to show the schema on the front-end
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register("category", views.CategoryView)
router.register("product", views.ProductView)
router.register("brand", views.BrandView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs", SpectacularSwaggerView.as_view(url_name="schema")),
]
