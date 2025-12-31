#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    # API endpoint for menu items to match client requests
    path('api/menu-items/', views.MenuItemsView.as_view()),
    # Detail endpoint for single menu item (GET/PUT/PATCH/DELETE)
    path('api/menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    # Allow slashless detail URL to avoid APPEND_SLASH redirect issue on DELETE
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
]
