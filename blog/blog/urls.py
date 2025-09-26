from django.urls import path
from .views import PostList, PostDetail, PostCreate,PostUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='postlist'),
    path('post/<int:pk>/', PostDetail.as_view(), name='postdetail'),
    path('post/create/', PostCreate.as_view(), name='newpost'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='editpost'),
    path('post/<int:pk>/delete/',PostDelete.as_view(), name='deletepost'),

]
