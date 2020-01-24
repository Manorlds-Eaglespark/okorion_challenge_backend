from django.urls import include, path
from .views import MyOwnView
from . import views

urlpatterns = [
    path('', MyOwnView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]