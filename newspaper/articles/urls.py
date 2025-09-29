from django.urls import path
from .views import CreateArticle, ListArticle, UpdateArticle, DeleteArticle, DetailArticle

urlpatterns = [
    path('createarticle/', CreateArticle.as_view(), name='articlecreate'),
    path('', ListArticle.as_view(), name='articlelist'),
    path('editarticle/<int:pk>/', UpdateArticle.as_view(), name='articleedit'),
    path('deletearticle/<int:pk>/', DeleteArticle.as_view(), name='articledelete'),
    path('detailarticle/<int:pk>/', DetailArticle.as_view(), name='articledetail',)

]
