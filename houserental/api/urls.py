from django import views
from django.contrib import admin
from .views import manage_house  # type: ignore
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import*
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,  # For logging in
    TokenRefreshView,     # For refreshing the JWT token
)


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),  # Include the URLs from myapp
]





from django.urls import path
from .views import manage_house, manage_booking, manage_review

urlpatterns = [
    path('house/', manage_house),
    path('house/<int:id>/', manage_house),
    path('booking/', manage_booking),
    path('booking/<int:id>/', manage_booking),
    path('review/', manage_review),
    path('review/<int:id>/', manage_review),
]