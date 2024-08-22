from django.contrib import admin
from django.urls import path, include
from product_app import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from payments import urls

# this is used to show the schema on the front-end
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register("category", views.CategoryView, basename="category")
router.register("product", views.ProductView, basename="product")
router.register("brand", views.BrandView, basename="brand")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/",include('rest_framework.urls')),
    path("user/",views.UserList.as_view()),
    path("user/<int:pk>",views.UserRetrieve.as_view()),
    
    
    # this link direct download a .yaml schema
    path("gettoken/",TokenObtainPairView.as_view(),name="token_obtain"),
    path("refreshtoken/",TokenRefreshView.as_view(),name="token_refresh"),
    path("verifytoken/",TokenVerifyView.as_view(),name="token_verify"),


    path('api/', include(urls)),


    path("schema", SpectacularAPIView.as_view(), name="schema"),
    path("schema/docs", SpectacularSwaggerView.as_view(url_name="schema")),
]
