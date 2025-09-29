from django.urls import path
from .views import CreateArticle

urlpatterns = [
    path('createarticle/', CreateArticle.as_view(), name='create'),
]
