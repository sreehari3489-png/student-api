from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()

router.register('students', StudentViewSet)


from django.urls import path

from .views import (
    register_view,
    login_view,
    home_view,
    logout_view,
    abc
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [

    path('', abc, name='abc'),

    path('register/', register_view, name='register'),

    path('login/', login_view, name='login'),

    path('home/', home_view, name='home'),

    path('logout/', logout_view, name='logout'),

    path('token/', TokenObtainPairView.as_view()),

    path('token/refresh/', TokenRefreshView.as_view()),

] + router.urls