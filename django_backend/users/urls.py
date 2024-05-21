from django.urls import path
from .views import UserCreate, BlacklistTokenUpdateView,  RegisterDoctorAPI, RegisterPatientAPI
from knox import views as knox_views
from .views import LoginAPI

app_name = 'users'

urlpatterns = [
    path('create/', UserCreate.as_view(), name="create_user"),
    path('create-doc/', RegisterDoctorAPI.as_view(), name="create_doc"),
    path('create-patient/', RegisterPatientAPI.as_view(), name="create_patient"),
    #path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         #name='blacklist'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('login/', LoginAPI.as_view(), name='login'),
]
