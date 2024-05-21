
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/", include("diseasepred.urls")),
    #path("accounts/", include("accounts.urls")),
    path("api/chats/", include("chats.urls")),
    #path('api-auth/', include('rest_framework.urls')),
    path('api/user/', include('users.urls', namespace='users')),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
